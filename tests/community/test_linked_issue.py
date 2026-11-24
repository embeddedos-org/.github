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


class SleepSpy:
    """Stands in for time.sleep so the retry tests record waits instead of taking them."""

    def __init__(self):
        self.waits = []

    def __call__(self, seconds):
        self.waits.append(seconds)


class LinkedIssuePolicyTest(unittest.TestCase):
    registry = {"trusted_automation_actors": ["dependabot[bot]"]}
    ATTEMPTS = MODULE.EMPTY_RESULT_ATTEMPTS

    def evaluate(self, event_payload, client, **kwargs):
        """Evaluate under the real retry policy, without the real waiting."""
        kwargs.setdefault("sleep", SleepSpy())
        return MODULE.evaluate(event_payload, self.registry, client, **kwargs)

    def test_exact_trusted_actor_is_exempt_without_api_call(self):
        client = FakeClient([])
        result = MODULE.evaluate(event("dependabot[bot]"), self.registry, client)
        self.assertIn("exempt", result)
        self.assertEqual(client.calls, [])

    def test_similar_actor_is_not_exempt(self):
        client = FakeClient([response([])] * self.ATTEMPTS)
        with self.assertRaisesRegex(MODULE.PolicyError, "must close"):
            self.evaluate(event("fake-dependabot[bot]"), client)
        self.assertEqual(len(client.calls), self.ATTEMPTS)

    def test_same_repository_closing_issue_passes(self):
        issue = {"number": 12, "url": "https://github.com/embeddedos-org/.github/issues/12", "repository": {"id": "R_same", "nameWithOwner": "embeddedos-org/.github"}}
        client = FakeClient([response([issue])])
        result = self.evaluate(event(), client)
        self.assertIn("issues/12", result)
        # A first-attempt pass must not cost a retry.
        self.assertEqual(len(client.calls), 1)

    def test_cross_repository_closing_issue_fails(self):
        # A cross-repository-only answer is already indexed, so it is decided on
        # the first attempt: waiting cannot turn it into a same-repository link.
        issue = {"number": 4, "url": "https://github.com/embeddedos-org/eos/issues/4", "repository": {"id": "R_other", "nameWithOwner": "embeddedos-org/eos"}}
        client = FakeClient([response([issue])])
        sleeper = SleepSpy()
        with self.assertRaisesRegex(MODULE.PolicyError, "same-repository"):
            self.evaluate(event(), client, sleep=sleeper)
        self.assertEqual(len(client.calls), 1)
        self.assertEqual(sleeper.waits, [])

    def test_missing_or_plain_mention_fails_when_github_recognizes_no_closer(self):
        client = FakeClient([response([])] * self.ATTEMPTS)
        with self.assertRaisesRegex(MODULE.PolicyError, "Fixes #123"):
            self.evaluate(event(), client)

    def test_paginates_closing_references(self):
        issue = {"number": 19, "url": "https://github.com/embeddedos-org/.github/issues/19", "repository": {"id": "R_same", "nameWithOwner": "embeddedos-org/.github"}}
        client = FakeClient([response([], next_cursor="cursor"), response([issue])])
        result = self.evaluate(event(), client)
        self.assertIn("issues/19", result)
        self.assertEqual(client.calls[1]["cursor"], "cursor")

    def test_api_failure_fails_closed(self):
        # A transport or GraphQL error is not index lag; it must not be retried
        # into a pass and must not be retried at all.
        client = FakeClient([MODULE.PolicyError("API unavailable")])
        sleeper = SleepSpy()
        with self.assertRaisesRegex(MODULE.PolicyError, "API unavailable"):
            self.evaluate(event(), client, sleep=sleeper)
        self.assertEqual(len(client.calls), 1)
        self.assertEqual(sleeper.waits, [])

    def test_malformed_event_fails_closed(self):
        with self.assertRaisesRegex(MODULE.PolicyError, "pull_request"):
            MODULE.evaluate({}, self.registry, FakeClient([]))


LAG_REGISTRY = {"trusted_automation_actors": ["dependabot[bot]"]}
LAG_ISSUE = {
    "number": 27,
    "url": "https://github.com/embeddedos-org/.github/issues/27",
    "repository": {"id": "R_same", "nameWithOwner": "embeddedos-org/.github"},
}


class GraphQLIndexLagTest(unittest.TestCase):
    """Issue #27: an empty closingIssuesReferences list may just be index lag.

    GitHub's GraphQL index trails pull request creation by up to about a
    minute, so the policy workflow - which starts seconds after the pull
    request is opened - could read an empty list for a body that plainly says
    ``Closes #N``, fail the pull request, and then pass on an identical re-run.
    These pin that an empty list is retried, that the retry is bounded, and
    that nothing else about the gate was loosened to achieve it.
    """

    registry = LAG_REGISTRY
    ISSUE = LAG_ISSUE

    def test_link_that_appears_on_a_later_attempt_passes(self):
        client = FakeClient([response([]), response([self.ISSUE])])
        sleeper = SleepSpy()
        result = MODULE.evaluate(event(), self.registry, client, sleep=sleeper)
        self.assertIn("issues/27", result)
        self.assertEqual(len(client.calls), 2)
        self.assertEqual(len(sleeper.waits), 1)

    def test_link_that_appears_on_the_last_attempt_passes(self):
        attempts = MODULE.EMPTY_RESULT_ATTEMPTS
        client = FakeClient([response([])] * (attempts - 1) + [response([self.ISSUE])])
        result = MODULE.evaluate(event(), self.registry, client, sleep=SleepSpy())
        self.assertIn("issues/27", result)
        self.assertEqual(len(client.calls), attempts)

    def test_retries_are_bounded_and_an_unlinked_pull_request_still_fails(self):
        attempts = MODULE.EMPTY_RESULT_ATTEMPTS
        client = FakeClient([response([])] * attempts)
        sleeper = SleepSpy()
        with self.assertRaisesRegex(MODULE.PolicyError, "must close"):
            MODULE.evaluate(event(), self.registry, client, sleep=sleeper)
        # Exactly `attempts` queries, and one fewer wait than queries: the
        # policy never sleeps after the decision it will act on.
        self.assertEqual(len(client.calls), attempts)
        self.assertEqual(len(sleeper.waits), attempts - 1)

    def test_the_policy_waits_before_giving_up(self):
        # A retry that does not wait does not outrun the index lag it exists
        # for, so the backoff being non-zero is part of the fix.
        attempts = MODULE.EMPTY_RESULT_ATTEMPTS
        client = FakeClient([response([])] * attempts)
        sleeper = SleepSpy()
        with self.assertRaises(MODULE.PolicyError):
            MODULE.evaluate(event(), self.registry, client, sleep=sleeper)
        self.assertTrue(all(wait > 0 for wait in sleeper.waits), sleeper.waits)
        self.assertGreaterEqual(sum(sleeper.waits), 30.0)

    def test_default_policy_retries_more_than_once(self):
        # Guards the constants themselves: dropping EMPTY_RESULT_ATTEMPTS to 1
        # would silently restore the old behaviour with every test still green.
        self.assertGreaterEqual(MODULE.EMPTY_RESULT_ATTEMPTS, 2)
        self.assertTrue(MODULE.EMPTY_RESULT_BACKOFF_SECONDS)

    def test_a_single_attempt_still_fails_an_unlinked_pull_request(self):
        client = FakeClient([response([])])
        sleeper = SleepSpy()
        with self.assertRaisesRegex(MODULE.PolicyError, "must close"):
            MODULE.evaluate(event(), self.registry, client, attempts=1, sleep=sleeper)
        self.assertEqual(len(client.calls), 1)
        self.assertEqual(sleeper.waits, [])

    def test_zero_attempts_is_refused_rather_than_passing_silently(self):
        with self.assertRaisesRegex(MODULE.PolicyError, "at least one attempt"):
            MODULE.evaluate(event(), self.registry, FakeClient([]), attempts=0)


if __name__ == "__main__":
    unittest.main()


class ReusableWorkflowGatesOnPullRequestState(unittest.TestCase):
    """The reusable workflow must not grade closed or merged pull requests.

    pull_request_target fires on `edited` for closed and merged PRs too. A
    merged PR cannot be changed to satisfy the policy, so the job carries a
    state guard. This pins the parsed structure, not the text: a guard that
    parses but lands on the wrong key, or on a step instead of the job, is
    the failure mode a substring check would miss.
    """

    WORKFLOW = ROOT / ".github" / "workflows" / "linked-issue-policy.yml"

    def _job(self):
        import yaml  # installed by community-governance-tests.yml

        with self.WORKFLOW.open(encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        return doc["jobs"]["linked-issue"]

    def test_job_runs_only_for_open_pull_requests(self):
        self.assertEqual(self._job().get("if"), "github.event.pull_request.state == 'open'")

    def test_guard_is_on_the_job_not_on_a_step(self):
        # A step-level `if` would still spin the job up and report a status
        # for a merged PR; the guard has to skip the job itself.
        for step in self._job()["steps"]:
            self.assertNotIn("if", step, step.get("name"))
