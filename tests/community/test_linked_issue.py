from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("validate_linked_issue", ROOT / "scripts" / "validate_linked_issue.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FakeClient:
    def __init__(self, responses):
        self.responses = iter(responses)
        self.calls = []

    def query(self, query, variables):
        self.calls.append(variables)
        response = next(self.responses)
        if isinstance(response, Exception):
            raise response
        return response


def event(actor="srpatcha"):
    return {
        "repository": {"name": ".github", "owner": {"login": "embeddedos-org"}},
        "pull_request": {"number": 7, "user": {"login": actor}},
    }


def response(nodes, *, repository_id="R_same", next_cursor=None):
    return {
        "repository": {
            "id": repository_id,
            "pullRequest": {
                "closingIssuesReferences": {
                    "nodes": nodes,
                    "pageInfo": {"hasNextPage": next_cursor is not None, "endCursor": next_cursor},
                }
            },
        }
    }


class LinkedIssuePolicyTest(unittest.TestCase):
    registry = {"trusted_automation_actors": ["dependabot[bot]"]}

    def test_exact_trusted_actor_is_exempt_without_api_call(self):
        client = FakeClient([])
        result = MODULE.evaluate(event("dependabot[bot]"), self.registry, client)
        self.assertIn("exempt", result)
        self.assertEqual(client.calls, [])

    def test_similar_actor_is_not_exempt(self):
        client = FakeClient([response([])])
        with self.assertRaisesRegex(MODULE.PolicyError, "must close"):
            MODULE.evaluate(event("fake-dependabot[bot]"), self.registry, client)
        self.assertEqual(len(client.calls), 1)

    def test_same_repository_closing_issue_passes(self):
        issue = {"number": 12, "url": "https://github.com/embeddedos-org/.github/issues/12", "repository": {"id": "R_same", "nameWithOwner": "embeddedos-org/.github"}}
        result = MODULE.evaluate(event(), self.registry, FakeClient([response([issue])]))
        self.assertIn("issues/12", result)

    def test_cross_repository_closing_issue_fails(self):
        issue = {"number": 4, "url": "https://github.com/embeddedos-org/eos/issues/4", "repository": {"id": "R_other", "nameWithOwner": "embeddedos-org/eos"}}
        with self.assertRaisesRegex(MODULE.PolicyError, "same-repository"):
            MODULE.evaluate(event(), self.registry, FakeClient([response([issue])]))

    def test_missing_or_plain_mention_fails_when_github_recognizes_no_closer(self):
        with self.assertRaisesRegex(MODULE.PolicyError, "Fixes #123"):
            MODULE.evaluate(event(), self.registry, FakeClient([response([])]))

    def test_paginates_closing_references(self):
        issue = {"number": 19, "url": "https://github.com/embeddedos-org/.github/issues/19", "repository": {"id": "R_same", "nameWithOwner": "embeddedos-org/.github"}}
        client = FakeClient([response([], next_cursor="cursor"), response([issue])])
        result = MODULE.evaluate(event(), self.registry, client)
        self.assertIn("issues/19", result)
        self.assertEqual(client.calls[1]["cursor"], "cursor")

    def test_api_failure_fails_closed(self):
        client = FakeClient([MODULE.PolicyError("API unavailable")])
        with self.assertRaisesRegex(MODULE.PolicyError, "API unavailable"):
            MODULE.evaluate(event(), self.registry, client)

    def test_malformed_event_fails_closed(self):
        with self.assertRaisesRegex(MODULE.PolicyError, "pull_request"):
            MODULE.evaluate({}, self.registry, FakeClient([]))


if __name__ == "__main__":
    unittest.main()
