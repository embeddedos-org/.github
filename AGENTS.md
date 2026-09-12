# Repository guidance

## Purpose

This repository is the organization-wide community health and governance control
plane for `embeddedos-org`. It contains policy, issue and pull request templates,
reusable workflows, the organization profile, and governance tooling. It does not
contain product source code; product changes belong in the repository that owns
the affected component.

## Source layout

- `profile/README.md` is the organization profile rendered by GitHub.
- Root community files provide organization defaults to repositories that do not
  define their own files.
- `.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md` define the
  organization issue and pull request intake contract.
- `.github/workflows/` contains this repository's checks and the reusable linked
  issue policy.
- `governance/repositories.json` is the authoritative repository registry;
  `governance/repositories.schema.json` defines its schema.
- `scripts/community_governance.py` audits live settings and renders rollout
  artifacts without silently overwriting divergent files.
- `templates/` and `wiki-templates/` are canonical rollout inputs.
- `docs/wiki/` is the source-controlled six-page Wiki snapshot rendered for this
  repository.
- `tests/community/` covers governance generation and linked-issue enforcement.
- `audit-2026-05/` is a frozen historical audit record, not current policy.

## Change rules

- Keep changes organization-wide and repository-agnostic unless a registry entry
  explicitly records a repository exception.
- Update the registry, schema, generator, templates, and tests together when a
  governance contract changes.
- Preserve the exact trusted automation allowlist and fail closed for human pull
  requests that do not close a same-repository issue.
- Pin reusable workflow consumers to a reviewed full commit SHA.
- Treat `wiki-templates/` as canonical and `docs/wiki/` as its rendered `.github`
  snapshot. Keep all six pages synchronized.
- The published GitHub Wiki is currently blocked because
  `https://github.com/embeddedos-org/.github.wiki.git` is unavailable. Do not
  claim that `docs/wiki/` has been published until that remote exists and the
  rendered pages have been pushed there.
- Do not rewrite or clean up baseline lint or canon debt in `audit-2026-05/` while
  making unrelated governance changes.
- Never place credentials, private vulnerability details, or production data in
  this public repository. Follow `SECURITY.md` for vulnerability reports.

## Validation

Run the focused community suite and documentation checks for governance changes:

```bash
python -m unittest discover -s tests/community -p "test_*.py" -v
python -c "from pathlib import Path; import yaml; \
files=Path('.github').rglob('*.yml'); \
[yaml.safe_load(path.read_text(encoding='utf-8')) for path in files]"
npx --yes markdownlint-cli2 "AGENTS.md" "docs/wiki/*.md"
git diff --check
```

Before requesting review, inspect the final diff and confirm that no
`audit-2026-05/` files changed. Push the existing feature branch normally, never
with force, and verify that pull request #6 remains open and draft, its remote
head matches the local commit, and its body retains `Fixes #5`.
