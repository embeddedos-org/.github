#!/usr/bin/env python3
"""Enforce a GitHub-recognized closing issue in the pull request repository."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Protocol


class PolicyError(RuntimeError):
    """Raised when policy inputs or GitHub data cannot be trusted."""


class GraphQLClient(Protocol):
    def query(self, query: str, variables: Mapping[str, Any]) -> Mapping[str, Any]: ...


@dataclass(frozen=True)
class HttpGraphQLClient:
    endpoint: str
    token: str

    def query(self, query: str, variables: Mapping[str, Any]) -> Mapping[str, Any]:
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps({"query": query, "variables": variables}).encode("utf-8"),
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
                "User-Agent": "embeddedos-linked-issue-policy",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.load(response)
        except (OSError, urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError) as error:
            raise PolicyError(f"GitHub GraphQL request failed: {error}") from error
        if payload.get("errors"):
            messages = "; ".join(str(item.get("message", item)) for item in payload["errors"])
            raise PolicyError(f"GitHub GraphQL returned errors: {messages}")
        data = payload.get("data")
        if not isinstance(data, dict):
            raise PolicyError("GitHub GraphQL response did not contain a data object")
        return data


QUERY = """
query LinkedIssues($owner: String!, $name: String!, $number: Int!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    id
    pullRequest(number: $number) {
      closingIssuesReferences(first: 100, after: $cursor) {
        nodes {
          number
          url
          repository { id nameWithOwner }
        }
        pageInfo { hasNextPage endCursor }
      }
    }
  }
}
"""


def load_json(path: Path) -> Mapping[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise PolicyError(f"Cannot read JSON from {path}: {error}") from error
    if not isinstance(value, dict):
        raise PolicyError(f"Expected a JSON object in {path}")
    return value


def event_identity(event: Mapping[str, Any]) -> tuple[str, str, int, str]:
    pull_request = event.get("pull_request")
    repository = event.get("repository")
    if not isinstance(pull_request, dict) or not isinstance(repository, dict):
        raise PolicyError("This policy requires a pull_request event payload")
    owner = repository.get("owner", {}).get("login")
    name = repository.get("name")
    number = pull_request.get("number")
    actor = pull_request.get("user", {}).get("login")
    if not isinstance(owner, str) or not owner or not isinstance(name, str) or not name:
        raise PolicyError("Event payload is missing the repository owner or name")
    if not isinstance(number, int) or number < 1:
        raise PolicyError("Event payload is missing a valid pull request number")
    if not isinstance(actor, str) or not actor:
        raise PolicyError("Event payload is missing the pull request author login")
    return owner, name, number, actor


def trusted_actors(registry: Mapping[str, Any]) -> frozenset[str]:
    actors = registry.get("trusted_automation_actors")
    if not isinstance(actors, list) or not actors or not all(isinstance(actor, str) and actor for actor in actors):
        raise PolicyError("Registry must contain a non-empty trusted_automation_actors list")
    if len(actors) != len(set(actors)):
        raise PolicyError("Registry trusted_automation_actors entries must be unique")
    return frozenset(actors)


def closing_issues(client: GraphQLClient, owner: str, name: str, number: int) -> tuple[str, list[Mapping[str, Any]]]:
    cursor: str | None = None
    repository_id: str | None = None
    issues: list[Mapping[str, Any]] = []
    while True:
        data = client.query(QUERY, {"owner": owner, "name": name, "number": number, "cursor": cursor})
        repository = data.get("repository")
        if not isinstance(repository, dict) or not isinstance(repository.get("id"), str):
            raise PolicyError(f"Repository {owner}/{name} was not returned by GitHub")
        if repository_id is None:
            repository_id = repository["id"]
        elif repository["id"] != repository_id:
            raise PolicyError("Repository identity changed while paginating closing references")
        pull_request = repository.get("pullRequest")
        if not isinstance(pull_request, dict):
            raise PolicyError(f"Pull request {owner}/{name}#{number} was not returned by GitHub")
        connection = pull_request.get("closingIssuesReferences")
        if not isinstance(connection, dict) or not isinstance(connection.get("nodes"), list):
            raise PolicyError("GitHub did not return closing issue references")
        issues.extend(node for node in connection["nodes"] if isinstance(node, dict))
        page_info = connection.get("pageInfo")
        if not isinstance(page_info, dict):
            raise PolicyError("GitHub did not return closing reference pagination data")
        if not page_info.get("hasNextPage"):
            break
        cursor = page_info.get("endCursor")
        if not isinstance(cursor, str) or not cursor:
            raise PolicyError("GitHub reported another page without a cursor")
    assert repository_id is not None
    return repository_id, issues


def evaluate(event: Mapping[str, Any], registry: Mapping[str, Any], client: GraphQLClient) -> str:
    owner, name, number, actor = event_identity(event)
    allowlist = trusted_actors(registry)
    if actor in allowlist:
        return f"trusted automation actor {actor} is exempt"

    repository_id, issues = closing_issues(client, owner, name, number)
    matches = [
        issue
        for issue in issues
        if isinstance(issue.get("repository"), dict)
        and issue["repository"].get("id") == repository_id
    ]
    if not matches:
        detail = "only cross-repository closing issues were recognized" if issues else "no closing issues were recognized"
        raise PolicyError(
            f"Pull request {owner}/{name}#{number} must close at least one same-repository issue; {detail}. "
            "Use Fixes #123, Closes #123, or Resolves #123 in the pull request body"
        )
    urls = ", ".join(str(issue.get("url", f"#{issue.get('number', '?')}")) for issue in matches)
    return f"same-repository closing issue found: {urls}"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--event", type=Path, required=True, help="Path to the GitHub event JSON")
    parser.add_argument("--registry", type=Path, required=True, help="Path to repositories.json")
    parser.add_argument("--api-url", default="https://api.github.com/graphql")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("policy error: GITHUB_TOKEN is required", file=sys.stderr)
        return 2
    try:
        message = evaluate(
            load_json(args.event),
            load_json(args.registry),
            HttpGraphQLClient(args.api_url, token),
        )
    except PolicyError as error:
        print(f"policy error: {error}", file=sys.stderr)
        return 1
    print(f"policy passed: {message}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
