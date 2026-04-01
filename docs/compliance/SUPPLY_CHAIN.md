# EoS Supply Chain Security

> **Document**: SUPPLY_CHAIN.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document covers EoS supply chain security practices including SBOM generation, dependency management, and trusted build infrastructure.

---

## Table of Contents

1. [Overview](#1-overview)
2. [NTIA SBOM Requirements](#2-ntia-sbom-requirements)
3. [SPDX Format](#3-spdx-format)
4. [CycloneDX Format](#4-cyclonedx-format)
5. [OpenChain (ISO/IEC 5230)](#5-openchain-isoiec-5230)
6. [ISO/IEC 20243 O-TTPS](#6-isoiec-20243-o-ttps)
7. [EoS Supply Chain Architecture](#7-eos-supply-chain-architecture)
8. [Compliance Matrix](#8-compliance-matrix)

---

## 1. Overview

Software supply chain security ensures the integrity, provenance, and trustworthiness of all components from source code to deployed artifacts. EoS implements supply chain security through SBOM generation, reproducible builds, dependency auditing, and transparent build infrastructure.

---

## 2. NTIA SBOM Requirements

The NTIA (National Telecommunications and Information Administration) defines minimum elements for Software Bill of Materials.

### Required Data Fields

| NTIA Field | EoS Implementation | Source |
|------------|---------------------|--------|
| **Supplier Name** | `EoS Project` / `embeddedos-org` | `NOTICE` files |
| **Component Name** | Repository name (e.g., `eos`, `eipc`) | `package.json`, `pyproject.toml`, `go.mod`, etc. |
| **Version** | Semantic version `0.1.0` | Build manifests |
| **Unique Identifier** | SPDX `SPDXRef-Package-*` or CycloneDX `bom-ref` | SBOM generation |
| **Dependency Relationship** | Direct + transitive dependencies | Lockfiles, `go.sum`, `pubspec.lock` |
| **Author** | `EoS Project Contributors` | `NOTICE`, `LICENSE` |
| **Timestamp** | ISO 8601 build timestamp | CI/CD metadata |

### NTIA Practices

| Practice | EoS Status |
|----------|------------|
| Automation — SBOM generated without human intervention | ✅ CI/CD pipeline |
| Frequency — SBOM updated on every release | ✅ Release workflow |
| Depth — includes transitive dependencies | ✅ Lockfile analysis |
| Known unknowns — documents components without analyzable deps | ✅ C repos documented manually |
| Distribution — SBOM available with release artifacts | ✅ Uploaded to GitHub Releases |
| Access control — SBOM available to downstream consumers | ✅ Public GitHub Releases |
| Mistake handling — process for correcting SBOM errors | ✅ Re-release workflow |

---

## 3. SPDX Format

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 5962:2021 |
| **Full Name** | Software Package Data Exchange |
| **Current Version** | SPDX 2.3 |
| **Formats** | JSON, RDF/XML, tag-value, XLSX |

### EoS SPDX Implementation

**Source-level**: Every source file includes an SPDX license header:
```c
// SPDX-License-Identifier: MIT
```

**Package-level**: SPDX document generated per release:
```json
{
  "spdxVersion": "SPDX-2.3",
  "dataLicense": "CC0-1.0",
  "SPDXID": "SPDXRef-DOCUMENT",
  "name": "eos-0.1.0",
  "documentNamespace": "https://github.com/embeddedos-org/eos/releases/v0.1.0",
  "creationInfo": {
    "created": "2026-03-31T00:00:00Z",
    "creators": ["Tool: ebuild-tool-0.1.0", "Organization: EoS Project"]
  },
  "packages": [
    {
      "SPDXID": "SPDXRef-Package-eos",
      "name": "eos",
      "versionInfo": "0.1.0",
      "supplier": "Organization: EoS Project",
      "downloadLocation": "https://github.com/embeddedos-org/eos/releases/tag/v0.1.0",
      "licenseConcluded": "MIT",
      "licenseDeclared": "MIT"
    }
  ]
}
```

### Per-Repo SPDX Mapping

| Repo | Package Manager | SPDX Generator |
|------|----------------|----------------|
| `eos`, `eboot`, `eai`, `eni`, `eos-platform`, `eos-sdk` | CMake | `cmake-spdx` / manual |
| `eosim`, `ebuild`, `ebuild-tool`, `EoSDesign` | pip/pyproject.toml | `spdx-tools-python` |
| `eipc` | Go modules | `spdx-sbom-generator` |
| `eApps` | Gradle/Kotlin | `spdx-gradle-plugin` |

---

## 4. CycloneDX Format

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Organization** | OWASP |
| **Current Version** | CycloneDX 1.5 |
| **Formats** | JSON, XML, Protocol Buffers |
| **Focus** | Security-oriented SBOM with VEX support |

### EoS CycloneDX Implementation

CycloneDX SBOMs are generated alongside SPDX for tool compatibility:

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "serialNumber": "urn:uuid:...",
  "version": 1,
  "metadata": {
    "timestamp": "2026-03-31T00:00:00Z",
    "component": {
      "type": "library",
      "name": "eos",
      "version": "0.1.0",
      "licenses": [{"license": {"id": "MIT"}}],
      "purl": "pkg:github/embeddedos-org/eos@0.1.0"
    }
  },
  "components": [],
  "vulnerabilities": []
}
```

### CycloneDX Advantages for EoS

| Feature | Benefit |
|---------|---------|
| VEX (Vulnerability Exploitability eXchange) | Communicate whether known CVEs affect EoS deployments |
| Formulation | Document build process and environment |
| Services | Describe `eipc` service endpoints |
| Cryptography BOM | Document `eos` crypto algorithm usage |

---

## 5. OpenChain (ISO/IEC 5230)

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 5230:2020 |
| **Full Name** | OpenChain Specification — Requirements for Open Source License Compliance |
| **Purpose** | Ensure consistent open source governance |

### EoS OpenChain Compliance

| OpenChain Requirement | EoS Implementation |
|-----------------------|---------------------|
| **Policy** — documented open source policy | ✅ `LICENSING.md` in `.github/docs/compliance/` |
| **Competence** — trained staff | ✅ `CONTRIBUTING.md` in each repo |
| **Awareness** — know the policy exists | ✅ README links to governance docs |
| **Scope** — defined program scope | ✅ All repos under `embeddedos-org` |
| **License identification** — SPDX headers | ✅ SPDX in every source file |
| **Compliance artifacts** — SBOM, NOTICE | ✅ `NOTICE`, `LICENSE`, SBOM in releases |
| **Community engagement** — upstream compliance | ✅ Dependency license audits in weekly CI |
| **Adherence** — ongoing compliance | ✅ CI enforcement, quarterly review |

---

## 6. ISO/IEC 20243 O-TTPS

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 20243:2018 |
| **Full Name** | Open Trusted Technology Provider Standard |
| **Purpose** | Mitigate risk of tainted/counterfeit components |

### EoS O-TTPS Alignment

| O-TTPS Requirement | EoS Implementation |
|--------------------|---------------------|
| **Secure development** | CI/CD with automated security scanning |
| **Secure engineering** | Code review via PR workflow |
| **Supply chain security** | Dependency auditing, lockfiles, SBOM |
| **Build integrity** | Reproducible builds via `ebuild`/`ebuild-tool` |
| **Delivery integrity** | SHA256 checksums on all release artifacts |
| **Vulnerability management** | `SECURITY.md`, 48-hour response SLA |
| **Malicious code prevention** | Automated scanning in weekly CI |
| **Tamper resistance** | Verified boot (`eboot`), HMAC integrity (`eipc`) |
| **Transparency** | Open source — full source code publicly available |

### EoS Trusted Build Pipeline

```
Source (GitHub) → CI Build (ebuild) → Test (QEMU/eosim) → Sign → Release (SHA256) → SBOM
     │                  │                    │                │          │
     └── Git history    └── Reproducible     └── Verified     └── Audit  └── Provenance
```

---

## 7. EoS Supply Chain Architecture

### Build Infrastructure

| Component | Role | Repo |
|-----------|------|------|
| `ebuild` | Build system definitions, platform configs | `ebuild` |
| `ebuild-tool` | Build automation CLI | `ebuild-tool` |
| GitHub Actions | CI/CD execution | `.github` (org workflows) |
| QEMU | Hardware emulation for testing | CI infrastructure |
| eosim | Product simulation | `eosim` |

### Dependency Categories

| Category | Examples | Audit Method |
|----------|----------|-------------|
| **Build tools** | CMake, Go, Python, Gradle | Version pinning, SHA verification |
| **Runtime dependencies** | None (zero-dependency embedded code) | N/A |
| **Test dependencies** | pytest, go test, JUnit | Weekly audit scan |
| **CI dependencies** | GitHub Actions | Version pinning (`@v4`), SHA pinning |

### Release Artifact Chain

Every EoS release includes:
1. **Source archive** — `.tar.gz` / `.zip` of source tree
2. **Binary artifacts** — per-platform compiled outputs
3. **SBOM** — SPDX + CycloneDX format
4. **Checksums** — SHA256 of all artifacts
5. **CHANGELOG** — human-readable changes
6. **NOTICE** — third-party attributions

---

## 8. Compliance Matrix

| Standard | Requirement | EoS Status |
|----------|-------------|------------|
| NTIA SBOM | Minimum data fields | ✅ All 7 fields populated |
| NTIA SBOM | Automation | ✅ CI-generated |
| NTIA SBOM | Transitive dependencies | ✅ Lockfile analysis |
| SPDX (ISO/IEC 5962) | License identification | ✅ SPDX headers in all files |
| SPDX (ISO/IEC 5962) | Package-level SBOM | ✅ Per-release |
| CycloneDX 1.5 | Security-oriented SBOM | ✅ VEX-ready |
| OpenChain (ISO/IEC 5230) | License compliance program | ✅ Documented policy + CI enforcement |
| ISO/IEC 20243 O-TTPS | Trusted provider | ✅ Transparent build, signed releases |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial supply chain security document |
