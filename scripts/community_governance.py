#!/usr/bin/env python3
"""Audit and stage EmbeddedOS community governance without mutating repositories."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


POLICY_SHA = re.compile(r"^[0-9a-f]{40}$")


class GovernanceError(RuntimeError):
    """Raised when audit or generation cannot proceed safely."""


@dataclass(frozen=True)
class GitHubRestClient:
    token: str
    api_url: str = "https://api.github.com"

    def get(self, path: str) -> Mapping[str, Any]:
        request = urllib.request.Request(
            f"{self.api_url.rstrip('/')}/{path.lstrip('/')}",
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "User-Agent": "embeddedos-community-governance-audit",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                value = json.load(response)
        except (OSError, urllib.error.HTTPError, urllib.error.URLError, json.JSONDecodeError) as error:
            raise GovernanceError(f"GitHub request failed for {path}: {error}") from error
        if not isinstance(value, dict):
            raise GovernanceError(f"Expected a JSON object from {path}")
        return value


def load_registry(path: Path) -> Mapping[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise GovernanceError(f"Cannot load registry {path}: {error}") from error
    if not isinstance(value, dict) or not isinstance(value.get("repositories"), list):
        raise GovernanceError("Registry must be an object containing repositories")
    return value


def audit(registry: Mapping[str, Any], client: GitHubRestClient) -> Mapping[str, Any]:
    organization = registry.get("organization")
    expected_features = registry.get("required_features")
    if not isinstance(organization, str) or not isinstance(expected_features, dict):
        raise GovernanceError("Registry organization or required_features is invalid")
    results: list[Mapping[str, Any]] = []
    for expected in registry["repositories"]:
        if not isinstance(expected, dict) or not isinstance(expected.get("name"), str):
            raise GovernanceError("Registry contains an invalid repository entry")
        live = client.get(f"repos/{organization}/{expected['name']}")
        observed = {
            "default_branch": live.get("default_branch"),
            "visibility": live.get("visibility", "private" if live.get("private") else "public"),
            "archived": live.get("archived"),
            "issues": live.get("has_issues"),
            "wiki": live.get("has_wiki"),
            "discussions": live.get("has_discussions"),
            "projects": live.get("has_projects"),
        }
        expected_values = {
            "default_branch": expected.get("default_branch"),
            "visibility": expected.get("visibility"),
            "archived": expected.get("lifecycle") == "archived",
            **expected_features,
        }
        differences = {
            key: {"expected": expected_values[key], "observed": observed.get(key)}
            for key in expected_values
            if observed.get(key) != expected_values[key]
        }
        results.append({"name": expected["name"], "observed": observed, "differences": differences})
    return {
        "organization": organization,
        "read_only": True,
        "repository_count": len(results),
        "conformant": all(not item["differences"] for item in results),
        "repositories": results,
        "project_v2_inventory": "blocked until a token with read:project is supplied",
    }


def render(text: str, repository: Mapping[str, Any], policy_sha: str) -> str:
    return (
        text.replace("{{repository}}", str(repository["name"]))
        .replace("{{default_branch}}", str(repository["default_branch"]))
        .replace("{{documentation_source}}", str(repository["documentation_source"]))
        .replace("POLICY_COMMIT_SHA", policy_sha)
    )


def generated_files(
    registry: Mapping[str, Any], templates: Path, policy_sha: str, names: list[str]
) -> dict[Path, str]:
    if not POLICY_SHA.fullmatch(policy_sha):
        raise GovernanceError("policy SHA must be a full lowercase 40-character commit SHA")
    entries = {item["name"]: item for item in registry["repositories"] if isinstance(item, dict)}
    selected = sorted(entries) if not names else names
    unknown = sorted(set(selected) - set(entries))
    if unknown:
        raise GovernanceError(f"Unknown repositories: {', '.join(unknown)}")
    files: dict[Path, str] = {}
    wiki_dir = templates / "wiki-templates"
    workflow_template = templates / "templates" / "workflows" / "linked-issue.yml"
    for name in selected:
        entry = entries[name]
        for source in sorted(wiki_dir.glob("*.md")):
            files[Path(name) / "docs" / "wiki" / source.name] = render(
                source.read_text(encoding="utf-8"), entry, policy_sha
            )
        files[Path(name) / ".github" / "workflows" / "linked-issue.yml"] = render(
            workflow_template.read_text(encoding="utf-8"), entry, policy_sha
        )
    return files


def write_staged(output: Path, files: Mapping[Path, str]) -> None:
    output = output.resolve()
    for relative, content in files.items():
        destination = (output / relative).resolve()
        if output != destination and output not in destination.parents:
            raise GovernanceError(f"Generated path escapes output root: {relative}")
        if destination.exists() and destination.read_text(encoding="utf-8") != content:
            raise GovernanceError(f"Refusing to overwrite divergent file: {destination}")
    for relative, content in files.items():
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            destination.write_text(content, encoding="utf-8")


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--registry", type=Path, default=Path("governance/repositories.json"))
    subparsers = result.add_subparsers(dest="command", required=True)

    audit_parser = subparsers.add_parser("audit", help="Read live repository settings and report differences")
    audit_parser.add_argument("--output", type=Path)
    audit_parser.add_argument("--write", action="store_true", help="Write the report to --output")

    generate_parser = subparsers.add_parser("generate", help="Render workflow and Wiki files into a staging root")
    generate_parser.add_argument("--templates", type=Path, default=Path("."))
    generate_parser.add_argument("--output", type=Path, required=True)
    generate_parser.add_argument("--policy-sha", required=True)
    generate_parser.add_argument("--repository", action="append", default=[])
    generate_parser.add_argument("--write", action="store_true", help="Create missing staged files")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv or sys.argv[1:])
    try:
        registry = load_registry(args.registry)
        if args.command == "audit":
            token = os.environ.get("GITHUB_TOKEN", "")
            if not token:
                raise GovernanceError("GITHUB_TOKEN is required for a live audit")
            report = audit(registry, GitHubRestClient(token))
            payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
            if args.output:
                if not args.write:
                    print(f"DRY RUN: would write audit report to {args.output}")
                else:
                    args.output.parent.mkdir(parents=True, exist_ok=True)
                    args.output.write_text(payload, encoding="utf-8")
            print(payload, end="")
            return 0 if report["conformant"] else 1

        files = generated_files(registry, args.templates, args.policy_sha, args.repository)
        for relative in files:
            print(f"{'WRITE' if args.write else 'DRY RUN'} {args.output / relative}")
        if args.write:
            write_staged(args.output, files)
        return 0
    except GovernanceError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
