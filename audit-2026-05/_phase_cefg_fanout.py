"""Phase C/E/F/G fan-out orchestrator.

For each of the 20 embeddedos-org repos:
  1. Clone (or fetch) into /home/spatchava/embeddedos-org/.audit-work/<repo>.
  2. Phase C: ensure .github/workflows/sync-release-branch.yml is present and equal to the canonical template.
  3. Phase E: ensure .github/dependabot.yml exists with the right ecosystems enabled per repo language.
  4. Phase F: ensure README.md begins with the canonical badge row + has a CI/release-model paragraph.
  5. Phase G: write embeddedos-org/.github/audit-2026-05/<repo>.md with the per-repo audit checklist (committed to the .github repo, not the product repo).
  6. Commit each repo locally and push to origin master.

Idempotent: re-running on a clean repo produces no commit.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ORG = "embeddedos-org"
WORK = Path("/home/spatchava/embeddedos-org/.audit-work")
GH_REPO = Path("/home/spatchava/embeddedos-org/.github-repo")
TEMPLATE_WORKFLOW = (GH_REPO / ".github/workflows/sync-release-branch.yml").read_text(encoding="utf-8")
TEMPLATE_DEPENDABOT = (GH_REPO / ".github/dependabot-template.yml").read_text(encoding="utf-8")
AUDIT_DIR = GH_REPO / "audit-2026-05" / "per-repo"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)

WORK.mkdir(parents=True, exist_ok=True)


def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=True, text=True)


def gh(args: list[str], parse: bool = False):
    out = run(["gh"] + args).stdout.strip()
    return json.loads(out) if parse else out


def clone_or_fetch(repo: str) -> Path:
    dst = WORK / repo
    if dst.exists():
        run(["git", "fetch", "--quiet", "origin"], cwd=dst, check=False)
        # Reset to origin/master to avoid stale local state.
        run(["git", "checkout", "master"], cwd=dst, check=False)
        run(["git", "reset", "--hard", "origin/master"], cwd=dst, check=False)
        return dst
    print(f"  cloning {repo}")
    run(["git", "clone", "--quiet", "--depth", "5",
         f"git@github.com:{ORG}/{repo}.git", str(dst)])
    return dst


# ---------------------------------------------------------------------------
# Phase C — sync-release-branch workflow
# ---------------------------------------------------------------------------

def apply_phase_c(repo_dir: Path) -> bool:
    """Return True if file was added or updated."""
    target = repo_dir / ".github" / "workflows" / "sync-release-branch.yml"
    target.parent.mkdir(parents=True, exist_ok=True)
    existing = target.read_text(encoding="utf-8") if target.exists() else None
    if existing == TEMPLATE_WORKFLOW:
        return False
    target.write_text(TEMPLATE_WORKFLOW, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Phase E — dependabot.yml customised per repo language
# ---------------------------------------------------------------------------

LANG_TO_ECOSYSTEMS = {
    "Python": ["pip"],
    "TypeScript": ["npm"],
    "JavaScript": ["npm"],
    "Go": ["gomod"],
    "C": [],
    "C++": [],
    "Dart": [],   # No dependabot ecosystem for pub yet
    "HTML": ["npm"],   # docs-style sites use npm for tooling
}


def apply_phase_e(repo_dir: Path, repo_name: str, language: str) -> bool:
    """Customise the dependabot template per detected language."""
    # Detect ecosystems by file presence — more robust than language guess.
    has_pyproject = (repo_dir / "pyproject.toml").exists() or (repo_dir / "requirements.txt").exists()
    has_package_json = (repo_dir / "package.json").exists()
    has_gomod = (repo_dir / "go.mod").exists()
    has_dockerfile = (repo_dir / "Dockerfile").exists()

    config = TEMPLATE_DEPENDABOT
    # Uncomment the ecosystems that apply to this repo by stripping the leading "  # " from those blocks.
    def uncomment_block(text: str, marker: str) -> str:
        # marker is the line "  # - package-ecosystem: <name>"
        # We uncomment that line and the next 11 lines (until the blank line before next block).
        lines = text.split("\n")
        out = []
        i = 0
        while i < len(lines):
            if marker in lines[i]:
                # Uncomment until next blank line
                while i < len(lines) and lines[i].strip() != "":
                    line = lines[i]
                    if line.startswith("  # "):
                        line = "  " + line[4:]  # strip "# "
                    elif line.startswith("  #"):
                        line = "  " + line[3:]
                    out.append(line)
                    i += 1
            else:
                out.append(lines[i])
                i += 1
        return "\n".join(out)

    if has_pyproject:
        config = uncomment_block(config, "package-ecosystem: pip")
    if has_package_json:
        config = uncomment_block(config, "package-ecosystem: npm")
    if has_gomod:
        config = uncomment_block(config, "package-ecosystem: gomod")
    if has_dockerfile:
        config = uncomment_block(config, "package-ecosystem: docker")

    target = repo_dir / ".github" / "dependabot.yml"
    target.parent.mkdir(parents=True, exist_ok=True)
    existing = target.read_text(encoding="utf-8") if target.exists() else None
    if existing == config:
        return False
    target.write_text(config, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Phase F — README badge row + release-model paragraph
# ---------------------------------------------------------------------------

BADGE_ROW_MARKER = "<!-- begin: org-uniform badges (audit-2026-05) -->"

def make_badge_row(repo_name: str) -> str:
    return (
        f"{BADGE_ROW_MARKER}\n"
        f"[![CI](https://github.com/{ORG}/{repo_name}/actions/workflows/ci.yml/badge.svg)](https://github.com/{ORG}/{repo_name}/actions/workflows/ci.yml)\n"
        f"[![CodeQL](https://github.com/{ORG}/{repo_name}/actions/workflows/codeql.yml/badge.svg)](https://github.com/{ORG}/{repo_name}/actions/workflows/codeql.yml)\n"
        f"[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/{ORG}/{repo_name}/badge)](https://securityscorecards.dev/viewer/?uri=github.com/{ORG}/{repo_name})\n"
        f"[![Release](https://img.shields.io/github/v/tag/{ORG}/{repo_name}?label=release&sort=semver)](https://github.com/{ORG}/{repo_name}/releases)\n"
        f"[![License](https://img.shields.io/github/license/{ORG}/{repo_name})](LICENSE)\n"
        "<!-- end: org-uniform badges (audit-2026-05) -->"
    )


RELEASE_MODEL_MARKER = "<!-- begin: release-model (audit-2026-05) -->"
RELEASE_MODEL = (
    f"{RELEASE_MODEL_MARKER}\n"
    "## Release model\n\n"
    "`master` is the line of development; every PR lands here. `release` is a\n"
    "rolling pointer to the latest released `vX.Y.Z` tag, updated automatically\n"
    "by [`.github/workflows/sync-release-branch.yml`](.github/workflows/sync-release-branch.yml).\n"
    "Tags are immutable.\n\n"
    "See [embeddedos-org/.github/STANDARDS.md](https://github.com/embeddedos-org/.github/blob/master/STANDARDS.md)\n"
    "for the org-wide tag scheme, release model, and the compliance frameworks\n"
    "every product targets.\n"
    "<!-- end: release-model (audit-2026-05) -->"
)


def apply_phase_f(repo_dir: Path, repo_name: str) -> bool:
    readme = repo_dir / "README.md"
    if not readme.exists():
        return False
    text = readme.read_text(encoding="utf-8")
    original = text
    badges = make_badge_row(repo_name)

    # Inject badges immediately after the first line that starts with "# " (the title).
    if BADGE_ROW_MARKER not in text:
        # Find the first H1
        m = re.search(r"^# .*$", text, re.MULTILINE)
        if m:
            insert_at = m.end()
            text = text[:insert_at] + "\n\n" + badges + "\n" + text[insert_at:]
        else:
            text = badges + "\n\n" + text

    # Append release model section before the License section if present, else at the end.
    if RELEASE_MODEL_MARKER not in text:
        # Try to insert before "## License" if present.
        m_license = re.search(r"^## License\b", text, re.MULTILINE)
        if m_license:
            insert_at = m_license.start()
            text = text[:insert_at] + RELEASE_MODEL + "\n\n" + text[insert_at:]
        else:
            text = text.rstrip() + "\n\n" + RELEASE_MODEL + "\n"

    if text == original:
        return False
    readme.write_text(text, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Phase G — per-repo audit checklist (written into the .github repo, not the product repo)
# ---------------------------------------------------------------------------

CHECKLIST_TEMPLATE = """\
# {repo} — audit checklist

> Generated as part of the 2026-05 production-readiness audit (Phase G).
> This file is the per-repo work-tracker the maintainer ticks off as the
> code/test/lint audit lands. The audit is multi-week by design — see
> [`production_readiness_20_repo_audit.plan.md`](../../C:/Users/spatchava/.llms/plans/production_readiness_20_repo_audit.plan.md).

## Repo facts

- Default branch: `master`
- Long-lived branches: `master`, `release`
- Primary language: `{language}`
- Latest tag at audit-start: `{latest_tag}`

## Phase C — release-branch sync

- [ ] `.github/workflows/sync-release-branch.yml` present (auto-fanned-out by Phase-C orchestrator)
- [ ] Tag round-trip verified: pushed a `v*-rc.0` tag, observed `release` branch move

## Phase E — CI / security baseline

- [ ] `ci.yml` runs on push and PR, exits 0
- [ ] `codeql.yml` enabled (or N/A for repos without supported language)
- [ ] `scorecard.yml` enabled
- [ ] `release.yml` triggers on `vX.Y.Z` tag push
- [ ] `.github/dependabot.yml` covers the right ecosystems
- [ ] No long-stale Dependabot PRs (none open >30 days)

## Phase F — README

- [ ] Title + tagline in first 2 lines
- [ ] Org-uniform badge row present (auto-injected)
- [ ] Release-model paragraph present (auto-injected)
- [ ] Elevator pitch makes no aspirational claims
- [ ] Quick-start runs on a clean machine
- [ ] Repository structure section accurate
- [ ] Standards-compliance section points at `embeddedos-org/.github/STANDARDS.md`
- [ ] Related-repos table is correct
- [ ] No links resolve to 404
- [ ] No reference to deprecated repo names (`eHardware-Designs-Products`, etc.)
- [ ] No inline `<style>` blocks that won't render on GitHub

## Phase G — code / test / lint

### Static analysis
- [ ] Linter for primary language passes on `master` (`ruff` / `clang-tidy` / `eslint` / `golangci-lint` / `dart analyze`)
- [ ] Format check passes (`black --check`, `clang-format --dry-run`, `prettier --check`, `gofmt -l`)

### Tests
- [ ] Test suite exists and is runnable from a clean clone
- [ ] Test suite passes locally on the latest tagged commit
- [ ] Code coverage measured and recorded somewhere

### Build
- [ ] Documented build command works on a clean machine (Linux baseline)
- [ ] Cross-compile (where applicable) at least one non-host target

### Smoke / integration
- [ ] Smoke test exists and passes on the latest tag
- [ ] Cross-repo integration via eFab profile (where applicable) passes

## Sign-off

When every checkbox above is ticked, append a line:

    Signed off vX.Y.Z @ <commit-sha> by <person> on <date>

…and commit to this file. The audit dir's rollup picks up signed-off repos
and excludes them from the next session's reopen list.
"""


def write_checklist(repo: str, language: str, latest_tag: str) -> Path:
    out = AUDIT_DIR / f"{repo}.md"
    out.write_text(
        CHECKLIST_TEMPLATE.format(repo=repo, language=language, latest_tag=latest_tag or "(none)"),
        encoding="utf-8",
    )
    return out


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def main() -> int:
    repos = json.loads(gh(["repo", "list", ORG, "--limit", "100", "--json", "name,primaryLanguage"]))
    skipped: list[str] = []

    # Skip the meta-repo itself (.github) for product-repo phases, but still write its checklist.
    for r in sorted(repos, key=lambda x: x["name"]):
        repo = r["name"]
        lang_obj = r.get("primaryLanguage") or {}
        language = lang_obj.get("name") if isinstance(lang_obj, dict) else "(unknown)"
        language = language or "(unknown)"
        print(f"\n=== {repo} ===")
        try:
            latest_tag = gh(["api", f"repos/{ORG}/{repo}/tags", "--jq", ".[0].name // empty"]) or ""
        except subprocess.CalledProcessError:
            latest_tag = ""

        # Always write the checklist (Phase G output, lives in .github repo).
        write_checklist(repo, language, latest_tag)

        # Skip self-modification of the .github repo (the orchestrator already lives there).
        if repo == ".github":
            print("  (skipping product-phase self-edits on .github)")
            continue

        try:
            d = clone_or_fetch(repo)
        except subprocess.CalledProcessError as e:
            print(f"  CLONE/FETCH FAILED: {e.stderr or e}")
            skipped.append(f"{repo}: clone failed")
            continue

        changed_c = apply_phase_c(d)
        changed_e = apply_phase_e(d, repo, language)
        changed_f = apply_phase_f(d, repo)

        if not (changed_c or changed_e or changed_f):
            print("  no changes (already conformant)")
            continue

        # Configure git identity then commit
        run(["git", "config", "user.name", "Srikanth Patchava"], cwd=d)
        run(["git", "config", "user.email", "Srikanth.Patchava@brooksautomation.com"], cwd=d)
        run(["git", "add", "-A"], cwd=d)
        msg_lines = ["chore(audit-2026-05): apply org-uniform CI/release/README baseline"]
        if changed_c:
            msg_lines.append("- Phase C: add .github/workflows/sync-release-branch.yml so release branch auto-tracks vX.Y.Z tags.")
        if changed_e:
            msg_lines.append("- Phase E: add .github/dependabot.yml with weekly cadence + correct ecosystems.")
        if changed_f:
            msg_lines.append("- Phase F: inject org-uniform README badge row + release-model section (idempotent markers).")
        msg_lines.append("")
        msg_lines.append("See embeddedos-org/.github/STANDARDS.md for the canonical release model and tag scheme.")
        msg_lines.append("This commit is part of the 2026-05 production-readiness audit.")
        try:
            run(["git", "commit", "-q", "-m", "\n\n".join(msg_lines)], cwd=d)
            run(["git", "push", "-q", "origin", "master"], cwd=d)
            print("  pushed")
        except subprocess.CalledProcessError as e:
            print(f"  PUSH FAILED: {e.stderr or e}")
            skipped.append(f"{repo}: push failed: {e.stderr or e}")

    print()
    print("=== summary ===")
    if skipped:
        print(f"skipped/failed ({len(skipped)}):")
        for s in skipped:
            print(f"  - {s}")
    else:
        print("All repos processed cleanly.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
