# ebuild — audit checklist

> Generated as part of the 2026-05 production-readiness audit (Phase G).
> This file is the per-repo work-tracker the maintainer ticks off as the
> code/test/lint audit lands. The audit is multi-week by design — see
> [`production_readiness_20_repo_audit.plan.md`](../../C:/Users/spatchava/.llms/plans/production_readiness_20_repo_audit.plan.md).

## Repo facts

- Default branch: `master`
- Long-lived branches: `master`, `release`
- Primary language: `C`
- Latest tag at audit-start: `v3.0.1`

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
