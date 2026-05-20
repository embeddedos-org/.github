# Per-repo README contract (v1, 2026-05)

Every canonical product README must contain the sections below in this order.
The org-wide audit (`embeddedos-org/.github/audit-2026-05/`) tracks compliance.

The Phase-F orchestrator (`_phase_f_readme_patch.py` in this dir) enforces the
**badge row** and the **CI / release model** paragraph by injecting them
idempotently at the top of every README that does not already contain them.
The remaining sections require per-repo authoring and are surfaced in the
per-repo audit checklist under `audit-2026-05/<repo>.md`.

## Mandatory sections (in order)

1. **Title + tagline**
   `# <Name>` followed by a single-line tagline that survives without context.

2. **Badge row** *(auto-injected if missing)*
   - CI status:        `![CI](https://github.com/embeddedos-org/<repo>/actions/workflows/ci.yml/badge.svg)`
   - CodeQL:           `![CodeQL](https://github.com/embeddedos-org/<repo>/actions/workflows/codeql.yml/badge.svg)`
   - Scorecard:        `![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/embeddedos-org/<repo>/badge)`
   - Latest release:   `![Release](https://img.shields.io/github/v/tag/embeddedos-org/<repo>?label=release&sort=semver)`
   - License:          `![License](https://img.shields.io/github/license/embeddedos-org/<repo>)`

3. **Elevator pitch** — 2–3 sentences. No aspirational content. Grounded in implemented reality.

4. **Quick start** — copy-paste-runnable on a clean machine.

5. **Repository structure** — top-level tree with one-line file purpose.

6. **CI / release model** *(auto-injected if missing)*
   Standard paragraph:
   > **Release model.** `master` is the line of development; every PR lands here.
   > `release` is a rolling pointer to the latest released `vX.Y.Z` tag, updated
   > automatically by `.github/workflows/sync-release-branch.yml`. Tags are
   > immutable. See [STANDARDS.md](https://github.com/embeddedos-org/.github/blob/master/STANDARDS.md)
   > for the org-wide tag scheme and compliance frameworks.

7. **Standards compliance** — pointer to `embeddedos-org/.github/STANDARDS.md` + the specific frameworks this repo claims to support.

8. **Related repos** — table linking to the org profile and sibling product repos.

9. **License + footer** — five-link footer used in the org profile:
   `[Website](https://embeddedos-org.github.io) · [Docs](https://embeddedos-org.github.io/docs/) · [Books](https://embeddedos-org.github.io/books.html) · [Stacks](https://embeddedos-org.github.io/stacks/) · [Org Profile](https://github.com/embeddedos-org)`

## Forbidden patterns

- Aspirational "production" claims for unimplemented features.
- Numeric claims that don't match repo reality (counted line counts, "60+ apps", etc.).
- Badge URLs referring to the pre-2026-05 repo names (`eHardware-Designs-Products`, etc.).
- References to dropped products (`eVera`, `eStocks`, `eHardware-Designs-Products`) outside the explicit canon exception in `docs/embeddedos-ecosystem-guide.md`.
- Inline `<style>` tags or HTML that won't render on GitHub.

## Compliance enforcement

- `check-product-canon.py` (in this repo) scans for forbidden patterns on every push.
- `lint-readme.yml` (in this repo) runs markdownlint + lychee link-check on every push touching `*.md`.
- The README contract is **not** automatically enforced beyond the badge row and release-model paragraph — section presence is an audit-time check, surfaced as a per-repo checklist.
