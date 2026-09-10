from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("community_governance", ROOT / "scripts" / "community_governance.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FakeRestClient:
    def __init__(self, values):
        self.values = values

    def get(self, path):
        return self.values[path]


class GovernanceConfigurationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / "governance" / "repositories.json").read_text(encoding="utf-8"))
        cls.schema = json.loads((ROOT / "governance" / "repositories.schema.json").read_text(encoding="utf-8"))

    def test_registry_validates_against_schema(self):
        jsonschema.validate(self.registry, self.schema)

    def test_registry_has_exact_authoritative_repositories(self):
        expected = {
            ".github", "EoSim", "EoStudio", "eAI", "eApps", "eBoot", "eBrowser",
            "eCAD-Hardware-Products", "eDB", "eFirmware", "eFlow", "eIPC", "eNI",
            "eNet", "eOffice", "eSec", "eVera", "ebuild", "embeddedos-org",
            "embeddedos-org.github.io", "embeddedos-stack", "eos", "eos-aero",
            "eos-health", "eosllm", "www.embeddedos.org",
        }
        names = [entry["name"] for entry in self.registry["repositories"]]
        self.assertEqual(set(names), expected)
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(len(names), 26)

    def test_visibility_and_default_branch_exceptions_are_exact(self):
        entries = {entry["name"]: entry for entry in self.registry["repositories"]}
        private = {name for name, entry in entries.items() if entry["visibility"] == "private"}
        main = {name for name, entry in entries.items() if entry["default_branch"] == "main"}
        self.assertEqual(private, {"eVera", "embeddedos-stack"})
        self.assertEqual(main, {"eos-health"})

    def test_trusted_bot_allowlist_is_exact(self):
        self.assertEqual(self.registry["trusted_automation_actors"], ["dependabot[bot]"])

    def test_issue_forms_are_valid_yaml_with_required_fields(self):
        forms = sorted((ROOT / ".github" / "ISSUE_TEMPLATE").glob("*.yml"))
        self.assertEqual({path.name for path in forms}, {"bug.yml", "config.yml", "documentation.yml", "feature.yml"})
        for path in forms:
            value = yaml.safe_load(path.read_text(encoding="utf-8"))
            self.assertIsInstance(value, dict, path)
        config = yaml.safe_load((ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml").read_text(encoding="utf-8"))
        self.assertFalse(config["blank_issues_enabled"])
        self.assertTrue(any("SECURITY.md" in link["url"] for link in config["contact_links"]))

    def test_pull_request_template_starts_with_required_contract(self):
        text = (ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("## Closing issue\n"))
        self.assertIn("Fixes #<same-repository issue number>", text)
        self.assertIn("Cross-repository", text)

    def test_workflow_never_checks_out_pull_request_code(self):
        reusable = (ROOT / ".github" / "workflows" / "linked-issue-policy.yml").read_text(encoding="utf-8")
        caller = (ROOT / ".github" / "workflows" / "linked-issue.yml").read_text(encoding="utf-8")
        self.assertIn("repository: embeddedos-org/.github", reusable)
        self.assertIn("persist-credentials: false", reusable)
        self.assertNotIn("github.event.pull_request.head", reusable)
        self.assertNotIn("checkout", caller.lower())
        self.assertNotIn("permissions: write", reusable)
        self.assertNotIn("write-all", reusable)

    def test_generator_dry_run_model_and_refusal_to_overwrite(self):
        files = MODULE.generated_files(self.registry, ROOT, "a" * 40, ["eos-health"])
        workflow = files[Path("eos-health/.github/workflows/linked-issue.yml")]
        self.assertIn("@" + "a" * 40, workflow)
        self.assertIn("policy_ref: " + "a" * 40, workflow)
        self.assertEqual(sum(path.suffix == ".md" for path in files), 6)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            MODULE.write_staged(output, files)
            target = output / "eos-health" / "docs" / "wiki" / "Home.md"
            target.write_text("local change\n", encoding="utf-8")
            with self.assertRaisesRegex(MODULE.GovernanceError, "Refusing to overwrite"):
                MODULE.write_staged(output, files)

    def test_audit_reports_feature_differences_without_writes(self):
        repo = self.registry["repositories"][0]
        registry = {"organization": "embeddedos-org", "required_features": self.registry["required_features"], "repositories": [repo]}
        live = {"default_branch": repo["default_branch"], "visibility": repo["visibility"], "archived": False, "has_issues": True, "has_wiki": False, "has_discussions": True, "has_projects": True}
        report = MODULE.audit(registry, FakeRestClient({"repos/embeddedos-org/.github": live}))
        self.assertTrue(report["read_only"])
        self.assertFalse(report["conformant"])
        self.assertEqual(report["repositories"][0]["differences"]["wiki"]["observed"], False)

    def test_wiki_template_set_and_links_are_complete(self):
        expected = {"Home.md", "Getting-Started.md", "Development.md", "Security.md", "FAQ.md", "_Sidebar.md"}
        templates = {path.name for path in (ROOT / "wiki-templates").glob("*.md")}
        self.assertEqual(templates, expected)
        sidebar = (ROOT / "wiki-templates" / "_Sidebar.md").read_text(encoding="utf-8")
        for page in ("Home", "Getting-Started", "Development", "Security", "FAQ"):
            self.assertIn(f"]({page})", sidebar)


if __name__ == "__main__":
    unittest.main()
