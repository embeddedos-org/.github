# EmbeddedOS — Standards Compliance

This file is the single source of truth for the standards the EmbeddedOS
organisation aims to satisfy across all 13 canonical product repositories.
Every product README references this file via a one-line pointer rather than
duplicating the list (which is how the list silently drifts out of date).

## Tag scheme

All canonical product repos tag releases as `vMAJOR.MINOR.PATCH` (SemVer):

    v0.1.0    v0.2.0    v1.0.0    v1.0.1    v1.1.0-rc.1    v1.1.0

Pre-release candidates use `-rc.N`. No other suffix is recognised by the
`release.yml` workflow or by the `sync-release-branch.yml` workflow.

### Documented exceptions (not in canon-13)

- `eosllm` — also tags VS-Code-extension artifacts as `vscode-vX.Y.Z` and
  browser-extension artifacts as `browser-vX.Y.Z`. Core library still tags
  plain `vX.Y.Z`.
- `www.embeddedos.org` — marketing site versions itself separately as
  `vX.Y.Z` starting from `v0.1.x`. Not part of the canonical 13-product
  versioning and not consumed downstream.
- `eApps` — historical pre-2026-05 tags (≈159 tags from before the new
  org-uniform release model). Old tags are immutable and not deleted; new
  tags follow the standard.

## Release model — master + release branch + immutable tags

Every repo has exactly two long-lived branches:

| Branch | What it is | Who writes to it |
|---|---|---|
| `master` | Line of development. Every PR merges here. | Maintainers via PRs. |
| `release` | Rolling pointer to the latest released `vX.Y.Z` tag. | The `sync-release-branch.yml` workflow only. **Never** push to it directly. |

When a `vX.Y.Z` tag is pushed on `master`, the `sync-release-branch.yml`
workflow force-updates `release` to point at the same commit. Tags are
immutable; the `release` branch is a movable pointer.

Consumers integrating with a product can pin to:
- A specific `vX.Y.Z` tag (most stable; recommended for production).
- The `release` branch (auto-tracks latest released).
- The `master` branch (development; may break).

## Org-wide compliance frameworks

Each product targets compliance with the subset that applies to its domain.
A repo's README declares which frameworks it claims to support.

- **Quality / engineering process**
  - [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html) — systems and software engineering — life cycle processes
  - [ISO/IEC 12207](https://www.iso.org/standard/63712.html) — software life cycle processes
  - [ISO/IEC 25000 (SQuaRE)](https://www.iso.org/standard/64764.html) — systems and software quality requirements and evaluation
  - [Conventional Commits 1.0.0](https://www.conventionalcommits.org/)
  - [Semantic Versioning 2.0.0](https://semver.org/)

- **Security**
  - [ISO/IEC 27001](https://www.iso.org/standard/27001) — information security management
  - [FIPS 140-3](https://csrc.nist.gov/Projects/Cryptographic-Module-Validation-Program) — cryptographic-module security
  - [OpenSSF Scorecard](https://github.com/ossf/scorecard) — automated repo-health checks
  - [CodeQL](https://codeql.github.com/) — static security analysis

- **Functional safety (domain-specific)**
  - [IEC 61508](https://webstore.iec.ch/publication/5515) — general-purpose functional safety
  - [ISO 26262](https://www.iso.org/standard/68383.html) — automotive functional safety
  - [DO-178C](https://www.rtca.org/training-and-resources/) — airborne software
  - [IEC 62304](https://www.iso.org/standard/38421.html) — medical device software

- **Accessibility**
  - [WCAG 2.1 AA](https://www.w3.org/TR/WCAG21/)

- **Supply chain transparency**
  - [SPDX](https://spdx.dev/) SBOM format
  - [CycloneDX](https://cyclonedx.org/) SBOM format
  - [NTIA Minimum Elements](https://www.ntia.gov/page/software-bill-materials) for an SBOM

- **Licensing**
  - All source code: [MIT License](https://opensource.org/licenses/MIT) unless a
    repo's `LICENSE` declares otherwise (`eCAD-Hardware-Products` is
    proprietary for the hardware schematics).
  - All documentation/books: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Org-wide files (inherited from `embeddedos-org/.github`)

Repos that do not ship their own override use these by default:

- `CODE_OF_CONDUCT.md` — Contributor Covenant 2.1
- `CONTRIBUTING.md` — short org-wide guide
- `SECURITY.md` — disclosure policy + response SLA
- `.github/ISSUE_TEMPLATE/config.yml` — issue routing
- `.github/PULL_REQUEST_TEMPLATE.md` — PR template
- `.github/dependabot-template.yml` — dependabot config template
- `.github/workflows/sync-release-branch.yml` — release-branch auto-sync
- `.github/workflows/check-canon.yml` — canonical-product-list validator

## Standards-compliance assertions

A repo asserts compliance with a framework by:
1. Adding it to the **Standards Compliance** section of its `README.md`.
2. Linking to evidence (a doc page, a CI workflow that enforces it, or an audit report).
3. Running the verifying workflow on every push (where automation exists).

A claim without (2) and (3) is **aspirational**, not asserted, and must be
labelled as such in the README so consumers are not misled.
