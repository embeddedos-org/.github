# EoS Open Source Governance

> **Document**: OSS_GOVERNANCE.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document covers EoS open source governance practices including OSI compliance, OpenChain conformance, SPDX policy, contribution workflows, and dependency management.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Open Source Initiative (OSI)](#2-open-source-initiative-osi)
3. [OpenChain Project (ISO/IEC 5230)](#3-openchain-project-isoiec-5230)
4. [SPDX Headers Policy](#4-spdx-headers-policy)
5. [Contribution Workflow](#5-contribution-workflow)
6. [CLA Process](#6-cla-process)
7. [Maintainer Responsibilities](#7-maintainer-responsibilities)
8. [Dependency Auditing](#8-dependency-auditing)
9. [NOTICE File Generation](#9-notice-file-generation)
10. [Compliance Matrix](#10-compliance-matrix)

---

## 1. Overview

EoS is developed as a fully open source project under the `embeddedos-org` GitHub organization. All repositories use the MIT license (OSI-approved). Governance practices ensure license compliance, transparent contribution processes, and responsible dependency management aligned with the OpenChain specification (ISO/IEC 5230).

### Governance Structure

```
embeddedos-org (GitHub Organization)
├── .github              — Org-level governance, templates, workflows
├── eos                  — Core kernel (C)
├── eboot                — Bootloader (C)
├── ebuild / ebuild-tool — Build system (Python/CMake)
├── eipc                 — IPC framework (Go/C)
├── eai                  — AI/ML framework (C)
├── eni                  — Neural interface (C)
├── eosim                — Simulator (Python)
├── eApps                — Applications (Kotlin/Compose)
├── eos-platform         — Platform configs (C/CMake)
├── eos-sdk              — SDK (C)
├── EoStudio             — IDE (Python)
└── embeddedos-org.github.io — Website (HTML/CSS)
```

---

## 2. Open Source Initiative (OSI)

### OSI Open Source Definition Compliance

The MIT license used by EoS satisfies all 10 criteria of the Open Source Definition:

| # | OSD Criterion | MIT License |
|:-:|---------------|:-----------:|
| 1 | Free redistribution | ✅ |
| 2 | Source code included | ✅ |
| 3 | Derived works permitted | ✅ |
| 4 | Integrity of author's source (patches allowed) | ✅ |
| 5 | No discrimination against persons or groups | ✅ |
| 6 | No discrimination against fields of endeavor | ✅ |
| 7 | Distribution of license (no additional license needed) | ✅ |
| 8 | License must not be specific to a product | ✅ |
| 9 | License must not restrict other software | ✅ |
| 10 | License must be technology-neutral | ✅ |

### OSI License Approval

| Attribute | Detail |
|-----------|--------|
| **License** | MIT License |
| **SPDX ID** | `MIT` |
| **OSI Approved** | ✅ Yes |
| **FSF Free** | ✅ Yes |
| **Debian Free** | ✅ Yes |
| **Fedora Good** | ✅ Yes |

---

## 3. OpenChain Project (ISO/IEC 5230)

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 5230:2020 |
| **Full Name** | OpenChain Specification — Requirements for open source license compliance programs |
| **Purpose** | Ensure quality and consistency in open source compliance |

### OpenChain Requirements — EoS Mapping

| Requirement | OpenChain Clause | EoS Implementation |
|-------------|------------------|---------------------|
| **Policy** | §3.1.1 | ✅ Documented in `LICENSING.md`, `OSS_GOVERNANCE.md` |
| **Competence** | §3.1.2 | ✅ `CONTRIBUTING.md` per repo with compliance guidance |
| **Awareness** | §3.1.3 | ✅ README links to governance docs; onboarding checklist |
| **Program scope** | §3.1.4 | ✅ All repos under `embeddedos-org` |
| **License identification** | §3.2.1 | ✅ SPDX headers in every source file |
| **Compliance artifacts** | §3.3.1 | ✅ SBOM (SPDX + CycloneDX), `NOTICE`, `LICENSE` per repo |
| **Community engagement** | §3.4.1 | ✅ Upstream contribution policy, dependency auditing |
| **Adherence** | §3.5.1 | ✅ CI enforcement, quarterly compliance reviews |

### OpenChain Conformance Evidence

| Evidence Type | Location |
|---------------|----------|
| Open source policy | `.github/docs/compliance/LICENSING.md` |
| Compliance program | `.github/docs/compliance/OSS_GOVERNANCE.md` |
| License identification | SPDX headers in source; `LICENSE` per repo |
| SBOM artifacts | GitHub Releases (SPDX + CycloneDX) |
| Contribution guidelines | `CONTRIBUTING.md` per repo |
| Security policy | `SECURITY.md` per repo |

---

## 4. SPDX Headers Policy

### Required Header Format

Every source file in the EoS ecosystem must include an SPDX license identifier as the first comment:

**C/C++/Go:**
```c
// SPDX-License-Identifier: MIT
```

**Python:**
```python
# SPDX-License-Identifier: MIT
```

**Kotlin:**
```kotlin
// SPDX-License-Identifier: MIT
```

**YAML/Shell:**
```yaml
# SPDX-License-Identifier: MIT
```

**HTML:**
```html
<!-- SPDX-License-Identifier: MIT -->
```

### Enforcement

| Mechanism | Scope | Frequency |
|-----------|-------|-----------|
| CI lint check | Every PR | Per-commit |
| Pre-commit hook | Local development | Per-commit |
| Weekly audit | All repos | Weekly |
| Manual review | Code review | Per-PR |

### Files Exempt from SPDX Headers

| File Type | Reason |
|-----------|--------|
| `LICENSE` | Contains the full license text |
| `NOTICE` | Attribution file |
| `.gitignore` | Configuration metadata |
| `*.json`, `*.yaml` (config) | Non-source data files |
| Binary files | Not human-readable source |
| Generated files | Auto-generated with proper attribution |

---

## 5. Contribution Workflow

### Pull Request Process

```
1. Fork repository
2. Create feature branch from `main`
3. Implement changes with SPDX headers
4. Run local tests and linting
5. Submit Pull Request
6. CI automated checks run:
   ├── Build verification
   ├── Unit tests
   ├── SPDX header check
   ├── License compatibility scan
   ├── Static analysis
   └── eosim simulation (if applicable)
7. Code review by maintainer(s)
8. Approval and merge
```

### Code Review Requirements

| Requirement | Details |
|-------------|---------|
| **Minimum reviewers** | 1 maintainer approval required |
| **CI status** | All checks must pass |
| **SPDX compliance** | SPDX header present in all new files |
| **License check** | No blocked licenses introduced |
| **Documentation** | Public API changes documented |
| **Tests** | New features require test coverage |
| **Changelog** | `CHANGELOG.md` updated for notable changes |

### CONTRIBUTING.md Template

Each repo includes a `CONTRIBUTING.md` covering:
- Development setup instructions
- Coding standards and style guide
- Testing requirements
- PR submission process
- SPDX header requirements
- License compatibility guidelines
- Code of conduct reference

---

## 6. CLA Process

### Contributor License Agreement

EoS uses the **Developer Certificate of Origin (DCO)** instead of a traditional CLA:

| Aspect | Detail |
|--------|--------|
| **Model** | DCO (Developer Certificate of Origin) v1.1 |
| **Mechanism** | `Signed-off-by` line in commit messages |
| **Enforcement** | DCO bot checks on every PR |
| **Purpose** | Certify contributor has rights to submit the code |

### DCO Sign-off

Contributors certify their submissions with:
```
Signed-off-by: Contributor Name <email@example.com>
```

Using `git commit -s` automatically adds the sign-off.

### DCO Text (v1.1)

The DCO certifies that:
1. The contribution was created in whole or in part by the contributor
2. The contributor has the right to submit it under the project's license
3. The contributor understands the contribution is public and a record is maintained

---

## 7. Maintainer Responsibilities

### Role Definitions

| Role | Responsibilities | Access Level |
|------|------------------|:------------:|
| **Owner** | Org-level governance, repo creation, policy decisions | Admin |
| **Maintainer** | Code review, merge authority, release management, security response | Write |
| **Contributor** | Bug reports, feature PRs, documentation | Fork + PR |
| **Reviewer** | Code review without merge authority | Read + Review |

### Maintainer Duties

| Duty | Frequency | Details |
|------|-----------|---------|
| PR review | Per-PR | Review within 3 business days |
| Security triage | On-report | Respond within 48 hours |
| Release management | Per-release | Tag, build, SBOM, CHANGELOG |
| Dependency audit | Weekly (CI) | Review automated audit reports |
| License review | Quarterly | Manual review of all dependencies |
| NOTICE file update | Per-release | Regenerate attributions |
| Documentation | Per-release | Update API docs, compliance docs |

### Bus Factor Mitigation

| Strategy | Implementation |
|----------|----------------|
| Multiple maintainers per repo | Minimum 2 maintainers |
| Cross-repo knowledge sharing | Quarterly knowledge transfer sessions |
| Documentation | Comprehensive `CODE_STRUCTURE.md` per repo |
| Automated processes | CI/CD reduces manual intervention needs |

---

## 8. Dependency Auditing

### Audit Process

| Phase | Tool | Frequency |
|-------|------|-----------|
| **License scan** | `license-checker`, SPDX tools | Per-PR (CI) |
| **Vulnerability scan** | Dependabot, `osv-scanner` | Daily (automated) |
| **Outdated check** | Dependabot, `pip-audit`, `go list` | Weekly |
| **Manual review** | Maintainer audit | Quarterly |

### Dependency Policy

| Category | Policy |
|----------|--------|
| **Approved licenses** | MIT, BSD-2, BSD-3, Apache-2.0, ISC, Zlib, Unlicense |
| **Restricted licenses** | LGPL (dynamic only), MPL-2.0, EPL-2.0 — requires review |
| **Blocked licenses** | GPL, AGPL, SSPL, BSL, Elastic, PolyForm |
| **Vulnerability policy** | Critical CVEs patched within 7 days |
| **Version pinning** | All deps version-pinned in lockfiles |
| **Transitive deps** | Audited for license and vulnerability |

### Per-Repo Dependency Tracking

| Repo | Package Manager | Lockfile | Audit Tool |
|------|----------------|----------|------------|
| `eos`, `eboot`, `eai`, `eni`, `eos-platform`, `eos-sdk` | CMake | N/A (vendored) | Manual |
| `eosim`, `ebuild-tool`, `EoStudio` | pip | `requirements.txt` / `pyproject.toml` | `pip-audit` |
| `eipc` | Go modules | `go.sum` | `govulncheck` |
| `eApps` | Gradle/Kotlin | `gradle.lockfile` | Gradle dependency verification |
| `embeddedos-org.github.io` | None | N/A | N/A (static HTML) |

---

## 9. NOTICE File Generation

### NOTICE File Contents

Each repo's `NOTICE` file includes:
1. **Project name and copyright** — EoS Project copyright statement
2. **License summary** — MIT license reference
3. **Third-party attributions** — Per-dependency: name, version, license, copyright holder

### NOTICE Template

```
EoS - Embedded Operating System
Copyright (c) 2026 EoS Project Contributors

This product is licensed under the MIT License.
See the LICENSE file for the full license text.

---

Third-Party Software Notices:

[Component Name] - [Version]
License: [SPDX ID]
Copyright: [Copyright Holder]
URL: [Repository/Homepage URL]

---
```

### Generation Process

| Step | Tool | Trigger |
|------|------|---------|
| Scan dependencies | `license-checker`, `pip-licenses`, `go-licenses` | Release workflow |
| Collect license texts | SPDX tools | Automated |
| Generate NOTICE | Custom script in CI | Per-release |
| Validate completeness | Manual maintainer review | Per-release |

---

## 10. Compliance Matrix

| Requirement | Standard | EoS Status |
|-------------|----------|------------|
| OSI-approved license (MIT) | OSD | ✅ Implemented |
| All 10 OSD criteria met | OSD | ✅ Implemented |
| OpenChain policy documented | ISO/IEC 5230 §3.1.1 | ✅ Implemented |
| OpenChain competence (contributor guides) | ISO/IEC 5230 §3.1.2 | ✅ Implemented |
| OpenChain awareness (README links) | ISO/IEC 5230 §3.1.3 | ✅ Implemented |
| OpenChain scope (all repos) | ISO/IEC 5230 §3.1.4 | ✅ Implemented |
| OpenChain license identification (SPDX) | ISO/IEC 5230 §3.2.1 | ✅ Implemented |
| OpenChain compliance artifacts (SBOM) | ISO/IEC 5230 §3.3.1 | ✅ Implemented |
| OpenChain community engagement | ISO/IEC 5230 §3.4.1 | ✅ Implemented |
| OpenChain adherence (CI + quarterly) | ISO/IEC 5230 §3.5.1 | ✅ Implemented |
| SPDX headers in every source file | SPDX / ISO 5962 | ✅ Implemented |
| SPDX CI enforcement | SPDX / ISO 5962 | ✅ Implemented |
| `LICENSE` file per repo | OSI / OpenChain | ✅ Implemented |
| `NOTICE` file per repo | Apache 2.0 compat / OpenChain | ✅ Implemented |
| `CONTRIBUTING.md` per repo | OpenChain | ✅ Implemented |
| `SECURITY.md` per repo | OpenChain | ✅ Implemented |
| DCO sign-off enforcement | DCO v1.1 | ✅ Implemented |
| Automated license scanning | OpenChain | ✅ CI pipeline |
| Automated vulnerability scanning | Industry best practice | ✅ Dependabot + osv-scanner |
| Quarterly manual audit | OpenChain | ✅ Scheduled |
| SBOM per release (SPDX + CycloneDX) | NTIA / ISO 5962 | ✅ Implemented |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial open source governance document |
# EoS Open Source Governance

> **Document**: OSS_GOVERNANCE.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document covers EoS open-source governance practices mapped to the Open Source Initiative (OSI) and OpenChain Project (ISO/IEC 5230).

---

## Table of Contents

1. [Overview](#1-overview)
2. [Open Source Initiative (OSI)](#2-open-source-initiative-osi)
3. [OpenChain Project (ISO/IEC 5230)](#3-openchain-project-isoiec-5230)
4. [EoS Governance Structure](#4-eos-governance-structure)
5. [Contribution Workflow](#5-contribution-workflow)
6. [Compliance Matrix](#6-compliance-matrix)

---

## 1. Overview

The EoS ecosystem is an open-source project licensed under MIT, hosted on GitHub at [github.com/embeddedos-org](https://github.com/embeddedos-org). This document defines how EoS aligns with international open-source governance standards and best practices.

### EoS Repository Portfolio

| Repo | Language | Domain |
|------|----------|--------|
| `eos` | C | Embedded OS kernel, HAL, drivers, services |
| `eboot` | C | Multi-stage bootloader with secure boot |
| `eipc` | Go | Inter-process communication framework |
| `eai` | C | Embedded AI inference layer |
| `eni` | C | Neural interface adapter |
| `ebuild` | Python | Build system definitions |
| `ebuild-tool` | Python | Build automation CLI |
| `eosim` | Python | Hardware simulator with GUI |
| `eAppSuite` | Kotlin | Cross-platform desktop/mobile apps |
| `eMobile-Apps` | Dart/Flutter | Mobile application suite |
| `EoSDesign` | Python | 2D/3D design tool with code generation |
| `eos-platform` | C | Platform abstraction layer |
| `eos-sdk` | C | SDK for EoS development |
| `embeddedos-org.github.io` | HTML | Project website |
| `.github` | YAML/MD | Organization-level config, templates, compliance docs |

---

## 2. Open Source Initiative (OSI)

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Organization** | Open Source Initiative |
| **Purpose** | Steward of the Open Source Definition (OSD) |
| **Founded** | 1998 |
| **Key Output** | Open Source Definition, OSI-approved license list |

### Open Source Definition Compliance

The OSI defines 10 criteria for open-source software. EoS compliance:

| # | OSD Criterion | EoS Status | Evidence |
|:-:|---------------|:----------:|----------|
| 1 | **Free Redistribution** | ✅ | MIT license imposes no redistribution restrictions |
| 2 | **Source Code** | ✅ | All source publicly available on GitHub |
| 3 | **Derived Works** | ✅ | MIT explicitly allows modifications and derived works |
| 4 | **Integrity of Author's Source** | ✅ | Git history preserves original authorship |
| 5 | **No Discrimination Against Persons or Groups** | ✅ | MIT has no discriminatory clauses |
| 6 | **No Discrimination Against Fields of Endeavor** | ✅ | MIT allows any use case (commercial, academic, government) |
| 7 | **Distribution of License** | ✅ | MIT automatically applies to recipients |
| 8 | **License Must Not Be Specific to a Product** | ✅ | MIT is product-independent |
| 9 | **License Must Not Restrict Other Software** | ✅ | MIT imposes no restrictions on other software |
| 10 | **License Must Be Technology-Neutral** | ✅ | MIT is technology-neutral |

### OSI License Approval

| Aspect | Detail |
|--------|--------|
| **EoS License** | MIT |
| **SPDX Identifier** | `MIT` |
| **OSI Approved** | ✅ Yes |
| **FSF Free** | ✅ Yes |
| **Debian Free** | ✅ Yes |
| **Fedora Allowed** | ✅ Yes |

---

## 3. OpenChain Project (ISO/IEC 5230)

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 5230:2020 |
| **Full Name** | Information Technology — OpenChain Specification |
| **Purpose** | International standard for open source license compliance programs |
| **Versions** | OpenChain 2.1 (ISO/IEC 5230:2020) |

### OpenChain Requirements Mapping

#### Requirement 1: Program Foundation

| Sub-Requirement | EoS Implementation |
|-----------------|---------------------|
| 1.1 — Policy | License strategy documented in `LICENSING.md` |
| 1.2 — Competence | `CONTRIBUTING.md` in each repo educates contributors |
| 1.3 — Awareness | README files link to governance documentation |
| 1.4 — Program scope | All repos under `embeddedos-org` GitHub organization |
| 1.5 — License obligations | MIT obligations (attribution) documented and enforced |

#### Requirement 2: Relevant Tasks

| Sub-Requirement | EoS Implementation |
|-----------------|---------------------|
| 2.1 — Access to external resources | SPDX license list, dependency scanners available |
| 2.2 — Effectively handle requests | `SECURITY.md` with 48-hour response SLA |

#### Requirement 3: Open Source Content Review and Approval

| Sub-Requirement | EoS Implementation |
|-----------------|---------------------|
| 3.1 — Bill of Materials (BOM) | SBOM generated per release (SPDX + CycloneDX) |
| 3.2 — License compliance | SPDX headers in all source files |
| 3.3 — License type identification | Automated license detection in weekly CI |
| 3.4 — Interaction with community | Issue tracker, PR workflow, CODE_OF_CONDUCT.md |

#### Requirement 4: Compliance Artifact Creation and Delivery

| Sub-Requirement | EoS Implementation |
|-----------------|---------------------|
| 4.1 — Compliance artifacts | `LICENSE`, `NOTICE`, `CHANGELOG`, SBOM per release |
| 4.2 — Artifact archive | GitHub Releases with permanent artifact storage |

#### Requirement 5: Understanding Open Source Community Engagements

| Sub-Requirement | EoS Implementation |
|-----------------|---------------------|
| 5.1 — Contributions | `CONTRIBUTING.md` with DCO (Developer Certificate of Origin) |
| 5.2 — Community participation | Public GitHub, issue tracking, PR reviews |

#### Requirement 6: Adherence to Policy Requirements

| Sub-Requirement | EoS Implementation |
|-----------------|---------------------|
| 6.1 — Conformance | Weekly CI enforces license compliance |
| 6.2 — Duration | Compliance maintained across all releases |

---

## 4. EoS Governance Structure

### Roles

| Role | Responsibilities | Scope |
|------|-----------------|-------|
| **Maintainer** | Review PRs, merge code, manage releases | Per-repo |
| **Committer** | Write access, code review | Per-repo |
| **Contributor** | Submit PRs, report issues | All repos |
| **User** | Use software, report bugs | All repos |

### Decision Making

| Decision Type | Process | Participants |
|--------------|---------|--------------|
| Bug fixes | PR review + CI pass | Maintainers |
| New features | Issue discussion → PR → review | Maintainers + Contributors |
| Architecture changes | RFC (issue/discussion) → consensus | All Maintainers |
| License changes | Full team vote (supermajority) | All Maintainers |
| Security issues | Private disclosure → fix → advisory | Security team |

### Repository Governance Files

Every EoS repository must contain:

| File | Purpose | Status |
|------|---------|:------:|
| `LICENSE` | MIT license text with SPDX header | ✅ All repos |
| `NOTICE` | Copyright and third-party attribution | ✅ All repos |
| `README.md` | Project description, badges, quick start | ✅ All repos |
| `CONTRIBUTING.md` | Contribution guidelines, DCO | ✅ All repos |
| `CODE_OF_CONDUCT.md` | Contributor Covenant v2.1 | ✅ All repos |
| `SECURITY.md` | Vulnerability disclosure policy | ✅ All repos |
| `CHANGELOG.md` | Keep a Changelog format | ✅ All repos |
| `.github/workflows/ci.yml` | CI pipeline | ✅ All repos |

---

## 5. Contribution Workflow

### PR Lifecycle

```
1. Fork → 2. Branch → 3. Code → 4. Test → 5. PR → 6. CI → 7. Review → 8. Merge
```

### Contribution Requirements

| Requirement | Enforcement |
|-------------|-------------|
| **DCO sign-off** | Required on all commits (`Signed-off-by:`) |
| **SPDX headers** | Required in new source files |
| **Tests** | CI must pass (unit + lint + build) |
| **Documentation** | Update README/docs for new features |
| **Changelog** | Add entry to CHANGELOG.md |
| **Code review** | At least one maintainer approval |
| **License compatibility** | New dependencies must be MIT-compatible |

### Code of Conduct Enforcement

| Level | Action | Applied For |
|-------|--------|-------------|
| 1 — Warning | Private written warning | First offense, minor violation |
| 2 — Temporary Ban | Temporary interaction ban | Repeated violations |
| 3 — Permanent Ban | Permanent removal | Severe/persistent violations |

Reports: **conduct@embeddedos.org**

---

## 6. Compliance Matrix

| Standard | Requirement | EoS Status |
|----------|-------------|:----------:|
| OSI OSD | 10 criteria for open-source | ✅ Full compliance |
| OSI License | MIT is OSI-approved | ✅ Approved |
| ISO/IEC 5230 §1 | Program foundation | ✅ Documented policy |
| ISO/IEC 5230 §2 | Relevant tasks | ✅ Process defined |
| ISO/IEC 5230 §3 | Content review | ✅ SBOM + SPDX |
| ISO/IEC 5230 §4 | Artifact delivery | ✅ GitHub Releases |
| ISO/IEC 5230 §5 | Community engagement | ✅ DCO + CONTRIBUTING |
| ISO/IEC 5230 §6 | Adherence | ✅ CI enforcement |

### Per-Repo Governance Checklist

| Repo | LICENSE | NOTICE | CONTRIBUTING | CODE_OF_CONDUCT | SECURITY | CHANGELOG |
|------|:-------:|:------:|:------------:|:---------------:|:--------:|:---------:|
| `eos` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `eboot` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `eipc` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `eai` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `eni` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ebuild` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ebuild-tool` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `eosim` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `eAppSuite` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `eMobile-Apps` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `EoSDesign` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `eos-platform` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `eos-sdk` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `embeddedos-org.github.io` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| `.github` | ✅ | ✅ | ✅ | ✅ | ✅ | N/A |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial open source governance document |
