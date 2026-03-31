# EoS Licensing Reference

> **Document**: LICENSING.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document provides a comprehensive reference for software license models, their compatibility with the EoS MIT license, and guidance for dependency management across the EoS ecosystem.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Permissive Licenses](#2-permissive-licenses)
3. [Copyleft Licenses](#3-copyleft-licenses)
4. [Weak Copyleft Licenses](#4-weak-copyleft-licenses)
5. [Source-Available Licenses](#5-source-available-licenses)
6. [Creative Commons Licenses](#6-creative-commons-licenses)
7. [Commercial Licenses](#7-commercial-licenses)
8. [EoS License Policy](#8-eos-license-policy)
9. [Dependency Compatibility Matrix](#9-dependency-compatibility-matrix)
10. [Compliance Matrix](#10-compliance-matrix)

---

## 1. Overview

All EoS repositories are licensed under the **MIT License** (SPDX: `MIT`). This permissive license maximizes adoption across commercial, academic, and open source contexts. When integrating third-party dependencies, license compatibility must be verified to ensure no conflicts with MIT distribution terms.

**EoS License Header** (required in every source file):
```
// SPDX-License-Identifier: MIT
```

---

## 2. Permissive Licenses

Permissive licenses impose minimal restrictions on redistribution. All are compatible with EoS's MIT license.

| License | SPDX ID | Key Terms | MIT Compatible | When to Use |
|---------|---------|-----------|:--------------:|-------------|
| **MIT** | `MIT` | Attribution required; no warranty | ✅ Yes | Default for all EoS code |
| **BSD 2-Clause** | `BSD-2-Clause` | Attribution; no endorsement clause omitted | ✅ Yes | Acceptable dependency |
| **BSD 3-Clause** | `BSD-3-Clause` | Attribution; no endorsement without permission | ✅ Yes | Acceptable dependency |
| **Apache 2.0** | `Apache-2.0` | Attribution; patent grant; NOTICE file required | ✅ Yes | Preferred for deps with patent clauses |
| **ISC** | `ISC` | Simplified BSD-style; attribution | ✅ Yes | Acceptable dependency |
| **zlib** | `Zlib` | Attribution in source only; altered versions marked | ✅ Yes | Compression libraries |
| **WTFPL** | `WTFPL` | No restrictions whatsoever | ✅ Yes | Use with caution — no patent/warranty terms |
| **The Unlicense** | `Unlicense` | Public domain dedication | ✅ Yes | Acceptable, verify jurisdiction |

### Permissive License Obligations for EoS

| Obligation | MIT | BSD-2 | BSD-3 | Apache 2.0 | ISC |
|------------|:---:|:-----:|:-----:|:----------:|:---:|
| Include license text | ✅ | ✅ | ✅ | ✅ | ✅ |
| Include copyright notice | ✅ | ✅ | ✅ | ✅ | ✅ |
| Include NOTICE file | — | — | — | ✅ | — |
| State changes | — | — | — | ✅ | — |
| Patent grant | — | — | — | ✅ | — |

---

## 3. Copyleft Licenses

Copyleft licenses require derivative works to be distributed under the same license. These are **incompatible** with distributing combined works under MIT.

| License | SPDX ID | Key Terms | MIT Compatible | When to Use |
|---------|---------|-----------|:--------------:|-------------|
| **GPL v2.0** | `GPL-2.0-only` | Derivatives must be GPL-2.0; source disclosure | ❌ No | Do NOT use as EoS dependency |
| **GPL v3.0** | `GPL-3.0-only` | Derivatives must be GPL-3.0; anti-tivoization | ❌ No | Do NOT use as EoS dependency |
| **LGPL v2.1** | `LGPL-2.1-only` | Dynamic linking permitted; static requires LGPL | ⚠️ Conditional | Only via dynamic linking |
| **LGPL v3.0** | `LGPL-3.0-only` | Dynamic linking permitted; installation info req | ⚠️ Conditional | Only via dynamic linking |
| **AGPL v3.0** | `AGPL-3.0-only` | Network use triggers copyleft; strongest copyleft | ❌ No | Do NOT use as EoS dependency |

### Copyleft Risk Assessment

| Risk Level | License | EoS Policy |
|:----------:|---------|------------|
| 🔴 High | GPL-2.0, GPL-3.0, AGPL-3.0 | **Blocked** — cannot be used in any EoS component |
| 🟡 Medium | LGPL-2.1, LGPL-3.0 | **Restricted** — dynamic linking only, requires review |
| 🟢 Low | All permissive | **Approved** — no restrictions |

---

## 4. Weak Copyleft Licenses

Weak copyleft applies copyleft only to modifications of the licensed code, not the larger work.

| License | SPDX ID | Key Terms | MIT Compatible | When to Use |
|---------|---------|-----------|:--------------:|-------------|
| **MPL 2.0** | `MPL-2.0` | File-level copyleft; larger work can be proprietary | ⚠️ Conditional | Modified MPL files must remain MPL |
| **EPL 2.0** | `EPL-2.0` | Module-level copyleft; secondary license option | ⚠️ Conditional | Requires legal review for linking |

### Weak Copyleft Obligations

| Obligation | MPL 2.0 | EPL 2.0 |
|------------|:-------:|:-------:|
| Modified files must retain license | ✅ | ✅ |
| Larger work can use different license | ✅ | ✅ |
| Source of modified files must be available | ✅ | ✅ |
| Patent grant | ✅ | ✅ |

---

## 5. Source-Available Licenses

Source-available licenses provide source access but restrict usage in ways incompatible with open source.

| License | SPDX ID | Key Terms | MIT Compatible | When to Use |
|---------|---------|-----------|:--------------:|-------------|
| **SSPL** | `SSPL-1.0` | Service providers must release entire stack | ❌ No | **Blocked** — not OSI-approved |
| **BSL 1.1** | `BUSL-1.1` | Usage restricted until change date | ❌ No | **Blocked** — non-free until conversion |
| **Elastic License 2.0** | `Elastic-2.0` | No competing SaaS; source available | ❌ No | **Blocked** — usage restrictions |
| **PolyForm** | `PolyForm-*` | Various non-compete/non-commercial variants | ❌ No | **Blocked** — non-free restrictions |

### Source-Available Policy

EoS **does not** permit source-available dependencies. These licenses restrict usage in ways that conflict with EoS's fully open MIT model. If a previously permissive dependency relicenses to source-available, EoS must fork from the last permissive version or find an alternative.

---

## 6. Creative Commons Licenses

Creative Commons licenses are designed for creative works, not software. EoS uses them for documentation and media assets only.

| License | SPDX ID | Key Terms | Use in EoS |
|---------|---------|-----------|------------|
| **CC0** | `CC0-1.0` | Public domain dedication | ✅ SBOM data license (SPDX documents) |
| **CC-BY 4.0** | `CC-BY-4.0` | Attribution required | ✅ Documentation, diagrams |
| **CC-BY-SA 4.0** | `CC-BY-SA-4.0` | Attribution + share-alike | ⚠️ Wiki contributions only |
| **CC-BY-NC 4.0** | `CC-BY-NC-4.0` | Attribution + non-commercial only | ❌ Not for EoS — restricts commercial use |
| **CC-BY-ND 4.0** | `CC-BY-ND-4.0` | Attribution + no derivatives | ❌ Not for EoS — restricts modification |

### EoS Documentation License

All EoS documentation is licensed under **CC-BY-4.0** unless otherwise noted. SPDX SBOM documents use **CC0-1.0** per SPDX specification requirements.

---

## 7. Commercial Licenses

Commercial licenses are proprietary and incompatible with open source distribution.

| License Model | Description | EoS Compatibility |
|---------------|-------------|-------------------|
| **EULA** | End-User License Agreement; restricts redistribution | ❌ Incompatible |
| **OEM** | Original Equipment Manufacturer; bundling rights | ❌ Incompatible |
| **SaaS** | Software-as-a-Service; no source distribution | ❌ Incompatible |
| **Freemium** | Free tier with paid features | ❌ Incompatible |

### Commercial Use of EoS

The MIT license explicitly permits commercial use. Third parties **may**:
- Use EoS in commercial products without royalties
- Modify and redistribute EoS under proprietary licenses
- Embed EoS in OEM devices
- Offer EoS-based SaaS services

The only requirement is preserving the MIT copyright and license notice.

---

## 8. EoS License Policy

### Approved Licenses for Dependencies

| Category | Licenses | Policy |
|----------|----------|--------|
| ✅ **Approved** | MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC, Zlib, Unlicense | No restrictions |
| ⚠️ **Restricted** | LGPL-2.1, LGPL-3.0, MPL-2.0, EPL-2.0 | Dynamic linking only; requires maintainer review |
| ❌ **Blocked** | GPL-2.0, GPL-3.0, AGPL-3.0, SSPL, BUSL, Elastic-2.0, PolyForm, CC-BY-NC, CC-BY-ND | Cannot be used in any EoS component |

### License Audit Process

1. **Automated scanning** — CI runs `license-checker` on every PR
2. **SPDX headers** — every source file must include `SPDX-License-Identifier: MIT`
3. **NOTICE generation** — `NOTICE` files list all third-party attributions
4. **Quarterly review** — manual audit of all dependencies across repos
5. **Escalation** — restricted licenses require maintainer + legal review

---

## 9. Dependency Compatibility Matrix

| EoS License (MIT) | Can use as dependency? | Can link statically? | Can link dynamically? | Must disclose source? |
|--------------------|:----------------------:|:--------------------:|:---------------------:|:---------------------:|
| MIT | ✅ | ✅ | ✅ | No |
| BSD-2-Clause | ✅ | ✅ | ✅ | No |
| BSD-3-Clause | ✅ | ✅ | ✅ | No |
| Apache-2.0 | ✅ | ✅ | ✅ | No (NOTICE required) |
| ISC | ✅ | ✅ | ✅ | No |
| Zlib | ✅ | ✅ | ✅ | No |
| Unlicense | ✅ | ✅ | ✅ | No |
| LGPL-2.1 | ⚠️ | ❌ | ✅ | Modified LGPL files only |
| LGPL-3.0 | ⚠️ | ❌ | ✅ | Modified LGPL files only |
| MPL-2.0 | ⚠️ | ⚠️ | ✅ | Modified MPL files only |
| EPL-2.0 | ⚠️ | ⚠️ | ✅ | Modified EPL files only |
| GPL-2.0 | ❌ | ❌ | ❌ | Entire combined work |
| GPL-3.0 | ❌ | ❌ | ❌ | Entire combined work |
| AGPL-3.0 | ❌ | ❌ | ❌ | Entire work + network use |
| SSPL | ❌ | ❌ | ❌ | Entire service stack |

---

## 10. Compliance Matrix

| Requirement | EoS Status |
|-------------|------------|
| All repos use OSI-approved license (MIT) | ✅ Implemented |
| SPDX headers in every source file | ✅ Implemented |
| `LICENSE` file in every repo root | ✅ Implemented |
| `NOTICE` file with third-party attributions | ✅ Implemented |
| Automated license scanning in CI | ✅ Implemented |
| Dependency license compatibility check | ✅ Implemented |
| Quarterly manual license audit | ✅ Implemented |
| Blocked license rejection in CI | ✅ Implemented |
| Restricted license escalation workflow | ✅ Implemented |
| SBOM includes license data (SPDX + CycloneDX) | ✅ Implemented |
| Documentation licensed under CC-BY-4.0 | ✅ Implemented |
| SBOM data licensed under CC0-1.0 | ✅ Implemented |
| Commercial use permitted without restriction | ✅ Inherent to MIT |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial licensing reference document |
# EoS License Compatibility & Strategy Guide

> **Document**: LICENSING.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document defines the EoS ecosystem licensing strategy, provides a comprehensive license compatibility matrix, and documents SPDX/SBOM practices.

---

## Table of Contents

1. [EoS License Strategy](#1-eos-license-strategy)
2. [Permissive Licenses](#2-permissive-licenses)
3. [Copyleft Licenses](#3-copyleft-licenses)
4. [Source-Available Licenses](#4-source-available-licenses)
5. [Creative Commons Licenses](#5-creative-commons-licenses)
6. [Commercial Licenses](#6-commercial-licenses)
7. [Standards & Tooling](#7-standards--tooling)
8. [Compatibility Matrix](#8-compatibility-matrix)
9. [Dependency Guidelines](#9-dependency-guidelines)

---

## 1. EoS License Strategy

### Primary License: MIT

All EoS repositories use the **MIT License** (SPDX: `MIT`) as the primary license.

**Rationale:**
- Maximum compatibility with commercial, open-source, and embedded deployments
- No copyleft obligations — downstream projects can use any license
- Simple, well-understood terms
- Compatible with all major RTOS and embedded ecosystems
- Suitable for safety-critical and regulated industries where license complexity is a barrier

**SPDX Header (required in every source file):**
```
// SPDX-License-Identifier: MIT
```

**Repository-level files:**

| File | Purpose |
|------|---------|
| `LICENSE` | Full MIT license text with SPDX identifier |
| `NOTICE` | Copyright attribution and third-party notices |
| `SPDX-License-Identifier` | Machine-readable header in each source file |

---

## 2. Permissive Licenses

Permissive licenses allow broad use, modification, and redistribution with minimal restrictions. All are **compatible** with EoS's MIT license.

| License | SPDX ID | OSI Approved | Key Terms | EoS Compatibility |
|---------|---------|:------------:|-----------|:------------------:|
| **MIT** | `MIT` | ✅ | Attribution only | ✅ Primary license |
| **BSD-2-Clause** | `BSD-2-Clause` | ✅ | Attribution only | ✅ Compatible |
| **BSD-3-Clause** | `BSD-3-Clause` | ✅ | Attribution + no endorsement clause | ✅ Compatible |
| **Apache-2.0** | `Apache-2.0` | ✅ | Attribution + patent grant + NOTICE file | ✅ Compatible |
| **ISC** | `ISC` | ✅ | Simplified MIT/BSD | ✅ Compatible |
| **zlib** | `Zlib` | ✅ | Attribution in source only | ✅ Compatible |
| **WTFPL** | `WTFPL` | ❌ | No restrictions | ✅ Compatible |
| **Unlicense** | `Unlicense` | ✅ | Public domain dedication | ✅ Compatible |

### Notes on Apache-2.0

Apache-2.0 includes an explicit patent grant, which MIT does not. When incorporating Apache-2.0 dependencies:
- Preserve the `NOTICE` file from the dependency
- The patent grant flows downstream
- Compatible with MIT for combined works

---

## 3. Copyleft Licenses

Copyleft licenses require derivative works to use the same or compatible license. **Exercise caution** when incorporating copyleft dependencies.

| License | SPDX ID | OSI Approved | Copyleft Scope | EoS Compatibility |
|---------|---------|:------------:|----------------|:------------------:|
| **GPL-2.0-only** | `GPL-2.0-only` | ✅ | Strong — entire derivative work | ⚠️ Caution |
| **GPL-3.0-only** | `GPL-3.0-only` | ✅ | Strong — entire derivative work + anti-TiVo | ⚠️ Caution |
| **LGPL-2.1-only** | `LGPL-2.1-only` | ✅ | Weak — library boundary | ✅ Dynamic link OK |
| **LGPL-3.0-only** | `LGPL-3.0-only` | ✅ | Weak — library boundary | ✅ Dynamic link OK |
| **AGPL-3.0-only** | `AGPL-3.0-only` | ✅ | Network — SaaS triggers copyleft | ❌ Avoid |
| **MPL-2.0** | `MPL-2.0` | ✅ | File-level copyleft | ✅ Compatible |
| **EPL-2.0** | `EPL-2.0` | ✅ | Module-level copyleft | ⚠️ Caution |

### EoS Policy on Copyleft

1. **GPL-2.0/3.0**: Do NOT statically link GPL code into EoS binaries. GPL code may be used as separate processes communicating via `eipc` IPC (process boundary = separate work).
2. **LGPL-2.1/3.0**: Dynamic linking is acceptable. Ensure end users can re-link against modified LGPL libraries.
3. **AGPL-3.0**: Prohibited in all EoS components. Network copyleft is incompatible with embedded deployments.
4. **MPL-2.0**: File-level copyleft is manageable — modified MPL files must remain MPL, but new files can be MIT.

---

## 4. Source-Available Licenses

Source-available licenses provide access to source code but impose restrictions that prevent them from qualifying as open source.

| License | SPDX ID | OSI Approved | Key Restrictions | EoS Compatibility |
|---------|---------|:------------:|------------------|:------------------:|
| **SSPL** | `SSPL-1.0` | ❌ | Service-level copyleft (MongoDB) | ❌ Avoid |
| **BSL 1.1** | `BUSL-1.1` | ❌ | Time-delayed open source | ⚠️ Check conversion date |
| **Elastic License 2.0** | `Elastic-2.0` | ❌ | No competing SaaS | ⚠️ Non-SaaS use may be OK |
| **PolyForm** | N/A | ❌ | Various (noncommercial, shield, etc.) | ❌ Avoid in production |

### EoS Policy on Source-Available

Source-available dependencies are **not permitted** in EoS core components (`eos`, `eboot`, `eipc`, `eos-sdk`). For tooling-only dependencies (build scripts, dev tools), BSL with a reasonable conversion date may be acceptable on a case-by-case basis.

---

## 5. Creative Commons Licenses

Creative Commons licenses are designed for creative works (documentation, media, data), **not software**.

| License | SPDX ID | OSI Approved | Permissions | EoS Use |
|---------|---------|:------------:|-------------|---------|
| **CC0-1.0** | `CC0-1.0` | ❌ (not software) | Public domain | ✅ Data/docs |
| **CC-BY-4.0** | `CC-BY-4.0` | ❌ | Attribution | ✅ Docs/media |
| **CC-BY-SA-4.0** | `CC-BY-SA-4.0` | ❌ | Attribution + ShareAlike | ⚠️ Docs only |
| **CC-BY-NC-4.0** | `CC-BY-NC-4.0` | ❌ | Attribution + NonCommercial | ❌ Avoid |
| **CC-BY-ND-4.0** | `CC-BY-ND-4.0` | ❌ | Attribution + NoDerivatives | ❌ Avoid |

### EoS Policy on Creative Commons

- **CC0 / CC-BY**: Acceptable for documentation, sample data, and media assets
- **CC-BY-SA**: Acceptable for standalone documentation (not embedded in software)
- **CC-BY-NC / CC-BY-ND**: Not permitted — restricts commercial use or modifications

---

## 6. Commercial Licenses

Commercial licenses are proprietary and require negotiation.

| License Type | Description | EoS Relevance |
|-------------|-------------|---------------|
| **EULA** | End User License Agreement | Downstream products built on EoS may use EULAs |
| **OEM** | Original Equipment Manufacturer license | Hardware vendors embedding EoS |
| **SaaS** | Software as a Service terms | Cloud-hosted EoS management tools |
| **Freemium** | Free tier + paid features | Potential model for EoS commercial support |

### EoS Dual-License Strategy

EoS uses MIT for all open-source distribution. Commercial entities may obtain:
- **Commercial support agreements** for production deployments
- **Certification packages** for safety-critical applications (IEC 61508, ISO 26262)
- **OEM licenses** with additional warranty and indemnification

The MIT license itself does not change — commercial offerings are for support, certification, and services.

---

## 7. Standards & Tooling

### SPDX (Software Package Data Exchange)

| Aspect | Detail |
|--------|--------|
| **Standard** | ISO/IEC 5962:2021 |
| **Format** | SPDX 2.3 (JSON, RDF, tag-value, XLSX) |
| **EoS Usage** | SPDX headers in all source files, SPDX SBOM generation in CI |
| **Identifier** | `SPDX-License-Identifier: MIT` |

### CycloneDX

| Aspect | Detail |
|--------|--------|
| **Standard** | OWASP CycloneDX v1.5 |
| **Format** | JSON, XML, Protocol Buffers |
| **EoS Usage** | CycloneDX SBOM generated alongside SPDX for maximum tool compatibility |
| **Components** | Dependencies, build tools, firmware components |

### OpenChain (ISO/IEC 5230)

| Aspect | Detail |
|--------|--------|
| **Standard** | ISO/IEC 5230:2020 |
| **Purpose** | Open source license compliance program |
| **EoS Alignment** | Documented license policy, SPDX identifiers, NOTICE files, dependency audits |

### OSI (Open Source Initiative)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Steward of the Open Source Definition |
| **EoS Alignment** | MIT is OSI-approved; all EoS repos meet the 10-point Open Source Definition |

### NTIA SBOM

| Aspect | Detail |
|--------|--------|
| **Source** | NTIA Minimum Elements for SBOM |
| **Required Fields** | Supplier, component name, version, unique ID, dependency relationship, author, timestamp |
| **EoS Compliance** | All fields populated via SPDX/CycloneDX generation in CI pipelines |

---

## 8. Compatibility Matrix

Can EoS (MIT) incorporate code under these licenses?

| Incoming License | Static Link | Dynamic Link | Separate Process | Documentation |
|-----------------|:-----------:|:------------:|:----------------:|:-------------:|
| MIT | ✅ | ✅ | ✅ | ✅ |
| BSD-2-Clause | ✅ | ✅ | ✅ | ✅ |
| BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| ISC | ✅ | ✅ | ✅ | ✅ |
| zlib | ✅ | ✅ | ✅ | ✅ |
| Unlicense | ✅ | ✅ | ✅ | ✅ |
| MPL-2.0 | ✅¹ | ✅ | ✅ | ✅ |
| LGPL-2.1 | ❌ | ✅ | ✅ | N/A |
| LGPL-3.0 | ❌ | ✅ | ✅ | N/A |
| GPL-2.0 | ❌ | ❌ | ✅ | N/A |
| GPL-3.0 | ❌ | ❌ | ✅ | N/A |
| AGPL-3.0 | ❌ | ❌ | ⚠️ | N/A |
| SSPL | ❌ | ❌ | ❌ | N/A |
| CC0 | ✅ | ✅ | ✅ | ✅ |
| CC-BY-4.0 | N/A | N/A | N/A | ✅ |
| CC-BY-SA-4.0 | N/A | N/A | N/A | ⚠️ |
| CC-BY-NC-4.0 | N/A | N/A | N/A | ❌ |

¹ MPL-2.0 modified files must remain MPL-2.0; new files can be MIT.

---

## 9. Dependency Guidelines

### Before Adding a Dependency

1. **Check the license** — verify SPDX identifier in the dependency's source
2. **Consult the matrix** — ensure compatibility per Section 8
3. **Document in NOTICE** — add attribution for all third-party code
4. **Update SBOM** — CI will regenerate, but verify after merge

### License Audit Process

```
Weekly CI → dependency scan → license extraction → compatibility check → report
```

- Automated via weekly CI workflows across all repos
- New dependencies with incompatible licenses will fail CI
- Quarterly manual review of all third-party licenses

### Per-Repo License Files

Every EoS repository must contain:

| File | Required | Purpose |
|------|:--------:|---------|
| `LICENSE` | ✅ | Full MIT license text |
| `NOTICE` | ✅ | Third-party attributions |
| `SPDX headers` | ✅ | In every source file |
| `CONTRIBUTING.md` | ✅ | License agreement for contributions (DCO) |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial license strategy and compatibility guide |
