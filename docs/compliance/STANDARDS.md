# EoS Standards Compliance Reference

> **Document**: STANDARDS.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document maps international standards to the EoS ecosystem, covering systems engineering, quality, security, safety, risk, platform, accessibility, benchmarking, and open source governance.

---

## Table of Contents

1. [Overview](#1-overview)
2. [Systems & Software Engineering](#2-systems--software-engineering)
3. [Quality & Testing](#3-quality--testing)
4. [Security](#4-security)
5. [Safety](#5-safety)
6. [Risk & Cloud](#6-risk--cloud)
7. [Usability & Innovation](#7-usability--innovation)
8. [Platform Standards](#8-platform-standards)
9. [Accessibility](#9-accessibility)
10. [Benchmarking](#10-benchmarking)
11. [Open Source Standards](#11-open-source-standards)
12. [Compliance Matrix](#12-compliance-matrix)

---

## 1. Overview

EoS aligns with internationally recognized standards to ensure the operating system meets requirements for safety-critical, security-sensitive, and quality-driven embedded deployments. Each standard is mapped to specific EoS repositories, modules, or processes.

---

## 2. Systems & Software Engineering

### ISO/IEC/IEEE 15288:2023 — Systems and Software Engineering — System Life Cycle Processes

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC/IEEE 15288:2023 |
| **Full Name** | Systems and software engineering — System life cycle processes |
| **Scope** | Defines processes for managing system lifecycle from concept through retirement |
| **EoS Alignment** | Product lifecycle managed via `ebuild` configs, `eosim` validation, CI/CD pipelines |
| **Applicable Repos** | `eos`, `ebuild`, `ebuild-tool`, `eosim`, `eos-platform` |

### ISO/IEC 12207 — Software Life Cycle Processes

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 12207:2017 |
| **Full Name** | Systems and software engineering — Software life cycle processes |
| **Scope** | Framework for software lifecycle including acquisition, supply, development, operation, maintenance |
| **EoS Alignment** | Development processes codified in `CONTRIBUTING.md`, CI/CD workflows, release management |
| **Applicable Repos** | All repos under `embeddedos-org` |

### ISO/IEC/IEEE 42010 — Architecture Description

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC/IEEE 42010:2022 |
| **Full Name** | Software, systems and enterprise — Architecture description |
| **Scope** | Conceptual model for architecture description of systems |
| **EoS Alignment** | Architecture documented via `CODE_STRUCTURE.md`, `docs/` directories, three-way alignment docs |
| **Applicable Repos** | `eos`, `eos-platform`, `eos-sdk`, `eai`, `eni`, `eipc` |

### ISO/IEC/IEEE 828 — Configuration Management

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC/IEEE 828:2021 |
| **Full Name** | Systems and software engineering — Configuration management |
| **Scope** | Planning and management of configuration identification, control, status accounting, audit |
| **EoS Alignment** | Git-based version control, semantic versioning, `CHANGELOG.md`, `build.yaml` per repo |
| **Applicable Repos** | All repos — enforced via `.github` org-level workflows |

### ISO/IEC 330xx — Process Assessment

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 33001–33099 series |
| **Full Name** | Information technology — Process assessment |
| **Scope** | Framework for assessing process capability and organizational maturity |
| **EoS Alignment** | Process maturity tracked via QMS document (`quality_management_system.md`), quarterly reviews |
| **Applicable Repos** | `.github` (org governance), `eos` (QMS docs) |

---

## 3. Quality & Testing

### ISO/IEC 25000 SQuaRE — Software Product Quality

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 25000:2014 |
| **Full Name** | Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) |
| **Scope** | Guide to SQuaRE series covering quality models, measurements, requirements, evaluation |
| **EoS Alignment** | Quality requirements documented in `ISO_25000_SQuaRE.md`, tracked across all repos |
| **Applicable Repos** | `eos` (docs), all repos (enforcement) |

### ISO/IEC 25010 — Quality Model

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 25010:2023 |
| **Full Name** | Systems and software engineering — Product quality model |
| **Scope** | Defines eight quality characteristics: functional suitability, performance, compatibility, usability, reliability, security, maintainability, portability |
| **EoS Alignment** | Each characteristic mapped to EoS metrics — boot time (performance), MPU isolation (security), HAL abstraction (portability) |
| **Applicable Repos** | `eos`, `eos-platform`, `eos-sdk` |

### ISO/IEC 25040 — Quality Evaluation

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 25040:2011 |
| **Full Name** | Systems and software engineering — Evaluation process |
| **Scope** | Process for evaluating software quality against defined requirements |
| **EoS Alignment** | CI/CD pipelines execute quality evaluation — unit tests, integration tests, static analysis, QEMU simulation |
| **Applicable Repos** | All repos with CI workflows |

### ISO/IEC/IEEE 29119 — Software Testing

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC/IEEE 29119:2022 (parts 1–5) |
| **Full Name** | Software and systems engineering — Software testing |
| **Scope** | Test processes, documentation, techniques, and keyword-driven testing |
| **EoS Alignment** | Test plans per repo, automated test execution in CI, QEMU/eosim hardware simulation testing |
| **Applicable Repos** | `eos`, `eboot`, `eai`, `eni`, `eipc`, `eosim` |

---

## 4. Security

### ISO/IEC 27001 — Information Security Management Systems

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 27001:2022 |
| **Scope** | Requirements for establishing, implementing, maintaining, and improving an ISMS |
| **EoS Alignment** | Security policies in `SECURITY.md`, access controls, audit logging, vulnerability management |
| **Applicable Repos** | All repos — org-level `SECURITY.md` |

### ISO/IEC 15408 — Common Criteria

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 15408:2022 (parts 1–3) |
| **Scope** | Evaluation criteria for IT security (EAL1–EAL7) |
| **EoS Alignment** | Security functional requirements mapped to kernel features — ACL, secure boot, crypto module |
| **Applicable Repos** | `eos`, `eboot` |

### ISO/IEC 20243 — O-TTPS

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 20243:2018 |
| **Scope** | Mitigate risk of tainted/counterfeit components in the supply chain |
| **EoS Alignment** | Covered in `SUPPLY_CHAIN.md` — reproducible builds, SBOM, signed releases |
| **Applicable Repos** | `ebuild`, `ebuild-tool`, `.github` |

### ISO/IEC 30111 — Vulnerability Handling

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 30111:2019 |
| **Scope** | Processes for vendors to handle vulnerability reports |
| **EoS Alignment** | 48-hour response SLA, private security advisory process, patch release workflow |
| **Applicable Repos** | All repos — `SECURITY.md` |

### ISO/IEC 29147 — Vulnerability Disclosure

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 29147:2018 |
| **Scope** | Guidelines for vendors on receiving and disclosing vulnerability information |
| **EoS Alignment** | Public `SECURITY.md` with disclosure instructions, GitHub Security Advisories |
| **Applicable Repos** | All repos |

### ISO/IEC 27701 — Privacy Information Management

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 27701:2019 |
| **Scope** | Extension to ISO 27001/27002 for privacy management |
| **EoS Alignment** | Minimal PII collection, telemetry opt-in only, privacy-by-design in `eai` inference |
| **Applicable Repos** | `eai`, `eos`, `eApps` |

### ISO/IEC 27040 — Storage Security

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 27040:2015 |
| **Scope** | Security for storage systems and infrastructures |
| **EoS Alignment** | dm-verity for filesystem integrity, encrypted partitions, keystore for credential storage |
| **Applicable Repos** | `eos`, `eboot` |

---

## 5. Safety

### IEC 61508 — Functional Safety

| Attribute | Detail |
|-----------|--------|
| **Reference** | IEC 61508:2010 (parts 1–7) |
| **Scope** | Functional safety of electrical/electronic/programmable electronic systems (SIL 1–4) |
| **EoS Alignment** | Safety-related software design, watchdog timers, redundancy, audit logging |
| **Applicable Repos** | `eos`, `eos-platform` (medical, industrial product profiles) |

### ISO 26262 — Automotive Functional Safety

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO 26262:2018 (parts 1–12) |
| **Scope** | Functional safety for road vehicles (ASIL A–D) |
| **EoS Alignment** | Automotive product profiles (`vehicle.py`), MPU isolation, safe-state transitions |
| **Applicable Repos** | `eos`, `eos-platform`, `eosim` (vehicle simulator) |

### DO-178C — Aerospace Software

| Attribute | Detail |
|-----------|--------|
| **Reference** | RTCA DO-178C / EUROCAE ED-12C |
| **Scope** | Software considerations in airborne systems certification (DAL A–E) |
| **EoS Alignment** | Traceability via build manifests, deterministic scheduling, test coverage requirements |
| **Applicable Repos** | `eos`, `eos-platform`, `eosim` (aircraft simulator) |

### EN 50128 — Railway Software

| Attribute | Detail |
|-----------|--------|
| **Reference** | EN 50128:2011 |
| **Scope** | Railway applications — software for railway control and protection systems (SIL 0–4) |
| **EoS Alignment** | Defensive coding, static analysis, formal verification readiness |
| **Applicable Repos** | `eos`, `eos-platform` |

---

## 6. Risk & Cloud

### ISO 31000 — Risk Management

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO 31000:2018 |
| **Scope** | Principles, framework, and process for managing risk |
| **EoS Alignment** | Risk register maintained in `risk_register.md`, quarterly risk reviews |
| **Applicable Repos** | `eos` (docs), `.github` (org governance) |

### ISO/IEC 17788 — Cloud Computing Overview

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 17788:2014 |
| **Scope** | Overview and vocabulary for cloud computing |
| **EoS Alignment** | Cloud-connected device profiles, OTA update infrastructure, telemetry services |
| **Applicable Repos** | `eipc`, `eos-platform`, `eai` |

### ISO/IEC 17789 — Cloud Reference Architecture

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 17789:2014 |
| **Scope** | Cloud computing reference architecture |
| **EoS Alignment** | Edge-cloud architecture via `eipc` gateway, device management, fleet telemetry |
| **Applicable Repos** | `eipc`, `eos-platform` |

---

## 7. Usability & Innovation

### ISO 9241 — Ergonomics of Human-Computer Interaction

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO 9241 series (parts 1–940) |
| **Scope** | Usability, accessibility, and human-centred design for interactive systems |
| **EoS Alignment** | EoStudio UI design, eApps Compose UI, CLI ergonomics, eosim GUI |
| **Applicable Repos** | `EoStudio`, `eApps`, `eosim`, `ebuild-tool` |

### ISO 56002 — Innovation Management

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO 56002:2019 |
| **Scope** | Guidance for establishing an innovation management system |
| **EoS Alignment** | Open contribution model, RFC process for new features, experimental product profiles |
| **Applicable Repos** | `.github` (org governance), all repos |

### ISO 9001 — Quality Management Systems

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO 9001:2015 |
| **Scope** | Requirements for quality management systems — customer focus, process approach, improvement |
| **EoS Alignment** | QMS document (`quality_management_system.md`), continuous improvement via CI/CD, defect tracking |
| **Applicable Repos** | `eos` (QMS docs), all repos (enforcement) |

---

## 8. Platform Standards

### POSIX — IEEE 1003

| Attribute | Detail |
|-----------|--------|
| **Reference** | IEEE 1003.1-2017 (POSIX.1) |
| **Scope** | Portable Operating System Interface — system interfaces, shell, utilities |
| **EoS Alignment** | POSIX compatibility layer (`examples/posix-app`), pthreads, semaphores, signals, file I/O, sockets |
| **Applicable Repos** | `eos`, `eos-platform` |

### Linux Standard Base (LSB)

| Attribute | Detail |
|-----------|--------|
| **Reference** | LSB 5.0 |
| **Scope** | Binary compatibility between Linux distributions — filesystem hierarchy, packaging, libraries |
| **EoS Alignment** | Linux HAL backend (`hal_linux.c`), FHS-compatible filesystem layout, systemd service integration |
| **Applicable Repos** | `eos`, `eos-platform` |

### FIPS 140-3

| Attribute | Detail |
|-----------|--------|
| **Reference** | FIPS 140-3 (NIST) |
| **Scope** | Security requirements for cryptographic modules |
| **EoS Alignment** | Crypto module design (SHA-256, AES-256, RSA/ECC), key management, HMAC authentication in `eipc` |
| **Applicable Repos** | `eos`, `eipc` |

---

## 9. Accessibility

### WCAG 2.1

| Attribute | Detail |
|-----------|--------|
| **Reference** | W3C WCAG 2.1 |
| **Scope** | Web Content Accessibility Guidelines — Level A, AA, AAA conformance |
| **EoS Alignment** | Website (`embeddedos-org.github.io`), eApps Compose UI, EoStudio, CLI tools |
| **Applicable Repos** | `embeddedos-org.github.io`, `eApps`, `EoStudio` |

---

## 10. Benchmarking

### SPEC — Standard Performance Evaluation Corporation

| Attribute | Detail |
|-----------|--------|
| **Reference** | SPEC benchmarks (CPU, power, embedded) |
| **Scope** | Standardized performance measurement methodologies |
| **EoS Alignment** | Boot time, context switch latency, IPC throughput, memory footprint benchmarks via `eosim` |
| **Applicable Repos** | `eosim`, `eos`, `eipc` |

---

## 11. Open Source Standards

### OSI — Open Source Initiative

| Attribute | Detail |
|-----------|--------|
| **Reference** | Open Source Definition (OSD) |
| **Scope** | Criteria for open source license approval |
| **EoS Alignment** | MIT license (OSI-approved), open development model |
| **Applicable Repos** | All repos |

### OpenChain (ISO/IEC 5230)

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 5230:2020 |
| **Scope** | Requirements for open source license compliance programs |
| **EoS Alignment** | SPDX headers, `NOTICE` files, dependency auditing, documented compliance program |
| **Applicable Repos** | All repos |

### NTIA SBOM

| Attribute | Detail |
|-----------|--------|
| **Reference** | NTIA Minimum Elements for SBOM |
| **Scope** | Minimum data fields and practices for software bill of materials |
| **EoS Alignment** | CI-generated SBOMs with all 7 required fields, transitive dependency analysis |
| **Applicable Repos** | All repos (via release workflows) |

### SPDX (ISO/IEC 5962)

| Attribute | Detail |
|-----------|--------|
| **Reference** | ISO/IEC 5962:2021 / SPDX 2.3 |
| **Scope** | Standard format for communicating software package licensing and origin |
| **EoS Alignment** | SPDX license headers in every source file, SPDX SBOM per release |
| **Applicable Repos** | All repos |

### CycloneDX

| Attribute | Detail |
|-----------|--------|
| **Reference** | CycloneDX 1.5 (OWASP) |
| **Scope** | Security-oriented SBOM format with VEX support |
| **EoS Alignment** | CycloneDX SBOMs generated alongside SPDX, VEX advisories |
| **Applicable Repos** | All repos (via release workflows) |

---

## 12. Compliance Matrix

| Standard | Category | EoS Status | Primary Repos |
|----------|----------|------------|----------------|
| ISO/IEC/IEEE 15288:2023 | Systems Engineering | ✅ Aligned | `eos`, `ebuild`, `eosim` |
| ISO/IEC 12207 | Software Engineering | ✅ Aligned | All repos |
| ISO/IEC/IEEE 42010 | Architecture | ✅ Aligned | `eos`, `eos-platform`, `eos-sdk` |
| ISO/IEC/IEEE 828 | Configuration Mgmt | ✅ Aligned | All repos |
| ISO/IEC 330xx | Process Assessment | 🔶 Partial | `.github`, `eos` |
| ISO/IEC 25000 SQuaRE | Quality | ✅ Aligned | All repos |
| ISO/IEC 25010 | Quality Model | ✅ Aligned | `eos`, `eos-platform` |
| ISO/IEC 25040 | Quality Evaluation | ✅ Aligned | All repos (CI) |
| ISO/IEC/IEEE 29119 | Testing | ✅ Aligned | `eos`, `eboot`, `eai`, `eni`, `eipc` |
| ISO/IEC 27001 | ISMS | ✅ Aligned | All repos |
| ISO/IEC 15408 | Common Criteria | 🔶 Partial | `eos`, `eboot` |
| ISO/IEC 20243 | O-TTPS | ✅ Aligned | `ebuild`, `.github` |
| ISO/IEC 30111 | Vulnerability Handling | ✅ Aligned | All repos |
| ISO/IEC 29147 | Vulnerability Disclosure | ✅ Aligned | All repos |
| ISO/IEC 27701 | Privacy | 🔶 Partial | `eai`, `eos` |
| ISO/IEC 27040 | Storage Security | ✅ Aligned | `eos`, `eboot` |
| IEC 61508 | Functional Safety | 🔶 Partial | `eos`, `eos-platform` |
| ISO 26262 | Automotive Safety | 🔶 Partial | `eos`, `eosim` |
| DO-178C | Aerospace | 📋 Planned | `eos`, `eosim` |
| EN 50128 | Railway | 📋 Planned | `eos`, `eos-platform` |
| ISO 31000 | Risk Management | ✅ Aligned | `eos` (docs) |
| ISO/IEC 17788 | Cloud Overview | ✅ Aligned | `eipc`, `eos-platform` |
| ISO/IEC 17789 | Cloud Architecture | 🔶 Partial | `eipc` |
| ISO 9241 | Ergonomics/HCI | 🔶 Partial | `EoStudio`, `eApps`, `eosim` |
| ISO 56002 | Innovation Mgmt | ✅ Aligned | `.github` (org) |
| ISO 9001 | QMS | ✅ Aligned | `eos` (QMS docs) |
| POSIX IEEE 1003 | Platform | ✅ Aligned | `eos`, `eos-platform` |
| Linux Standard Base | Platform | ✅ Aligned | `eos`, `eos-platform` |
| FIPS 140-3 | Crypto | 🔶 Partial | `eos`, `eipc` |
| WCAG 2.1 | Accessibility | 🔶 Partial | `embeddedos-org.github.io`, `eApps` |
| SPEC | Benchmarking | ✅ Aligned | `eosim`, `eos` |
| OSI | Open Source | ✅ Aligned | All repos |
| OpenChain (ISO/IEC 5230) | OSS Governance | ✅ Aligned | All repos |
| NTIA SBOM | Supply Chain | ✅ Aligned | All repos |
| SPDX (ISO/IEC 5962) | License ID | ✅ Aligned | All repos |
| CycloneDX | Security SBOM | ✅ Aligned | All repos |

**Legend**: ✅ Aligned — fully implemented | 🔶 Partial — partially implemented, work in progress | 📋 Planned — planned for future release

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial standards compliance reference |
# EoS Standards Alignment & Compliance Matrix

> **Document**: STANDARDS.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document maps the EoS ecosystem to international standards for systems engineering, software quality, security, safety, and governance.

---

## Table of Contents

1. [Systems & Software Engineering](#1-systems--software-engineering)
2. [Process Assessment](#2-process-assessment)
3. [Software Quality](#3-software-quality)
4. [Information Security](#4-information-security)
5. [Risk Management](#5-risk-management)
6. [Vulnerability Handling](#6-vulnerability-handling)
7. [Testing](#7-testing)
8. [Privacy](#8-privacy)
9. [Data Security](#9-data-security)
10. [Cloud Computing](#10-cloud-computing)
11. [Usability](#11-usability)
12. [Innovation](#12-innovation)
13. [Quality Management](#13-quality-management)
14. [Functional Safety](#14-functional-safety)
15. [Compliance Matrix](#15-compliance-matrix)

---

## 1. Systems & Software Engineering

### ISO/IEC/IEEE 15288:2023 — Systems and Software Engineering — System Life Cycle Processes

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC/IEEE 15288:2023 |
| **Title** | Systems and Software Engineering — System Life Cycle Processes |
| **Category** | Systems Engineering |
| **EoS Alignment** | EoS follows a full system life cycle from concept (EoSDesign product profiles) through implementation (eos kernel, eboot bootloader), integration (eipc, eni, eai), validation (eosim simulation), deployment (ebuild/ebuild-tool), and operation (eAppSuite, eMobile-Apps). Each repo has CI/CD pipelines implementing continuous verification. The `eos-platform` repo defines platform integration activities. |
| **Relevant Repos** | `eos`, `eboot`, `eipc`, `eai`, `eni`, `ebuild`, `ebuild-tool`, `eosim`, `eos-platform`, `EoSDesign` |

### ISO/IEC 12207 — Systems and Software Engineering — Software Life Cycle Processes

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 12207 |
| **Title** | Systems and Software Engineering — Software Life Cycle Processes |
| **Category** | Software Engineering |
| **EoS Alignment** | Each EoS repository follows defined software processes: requirements (product profiles in `eos/products/`), design (architecture docs), implementation (source code with coding standards), testing (unit/integration/QEMU/eosim tests), maintenance (CHANGELOG, SECURITY.md, versioning). The `.github` org repo provides cross-cutting process templates. |
| **Relevant Repos** | All repositories |

### ISO/IEC/IEEE 42010 — Architecture Description

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC/IEEE 42010 |
| **Title** | Systems and Software Engineering — Architecture Description |
| **Category** | Architecture |
| **EoS Alignment** | Architecture is documented at multiple levels: system-level architecture in `embeddedos-org.github.io` (ecosystem flow diagram), per-repo architecture docs (`eipc/README.md` architecture diagram, `eAppSuite/docs/architecture.md`, `eMobile-Apps/docs/architecture.md`), and product-specific views via `EoSDesign` product designer. Viewpoints cover hardware abstraction (HAL), communication (IPC), AI/ML pipeline, and user interface layers. |
| **Relevant Repos** | `.github`, `embeddedos-org.github.io`, `eipc`, `eAppSuite`, `eMobile-Apps`, `EoSDesign` |

### ISO/IEC/IEEE 828 — Configuration Management

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC/IEEE 828 |
| **Title** | Systems and Software Engineering — Configuration Management |
| **Category** | Configuration Management |
| **EoS Alignment** | All repos use Git version control with `master` as the canonical branch. Semantic Versioning (SemVer) is applied consistently at v0.1.0. Build configuration is managed through `build.yaml` files per C repo, `pyproject.toml` for Python repos, `gradle.properties` for Kotlin, `pubspec.yaml` for Flutter, and `go.mod` for Go. CI/CD pipelines enforce build reproducibility. Release artifacts include SHA256 checksums. |
| **Relevant Repos** | All repositories |

---

## 2. Process Assessment

### ISO/IEC 330xx Series — Process Assessment

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 33001, 33002, 33003, 33004, 33020 |
| **Title** | Information Technology — Process Assessment |
| **Category** | Process Assessment |
| **EoS Alignment** | EoS processes are assessed through automated CI/CD metrics: build pass rates (nightly/weekly), test coverage, linting compliance (flake8, mypy, detekt, dart analyze), and dependency audit results. Process capability is measured by the maturity of each repo's CI pipeline — from Level 1 (basic CI) to Level 3 (nightly + weekly + QEMU sanity + eosim integration). The `.github` org provides standardized workflow templates ensuring process consistency. |
| **Relevant Repos** | `.github`, all repositories with CI/CD |

---

## 3. Software Quality

### ISO/IEC 25000 (SQuaRE) — Systems and Software Quality Requirements and Evaluation

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 25000 |
| **Title** | Systems and Software Quality Requirements and Evaluation (SQuaRE) |
| **Category** | Software Quality |
| **EoS Alignment** | The SQuaRE framework guides EoS quality planning. Quality requirements are captured in product profiles (`eos/products/*.h`), evaluated through automated test suites, and reported via CI artifacts. Quality models are applied per component: reliability for `eos` kernel, performance for `eipc` transport, usability for `eAppSuite`/`eMobile-Apps`/`EoSDesign`. |
| **Relevant Repos** | All repositories |

### ISO/IEC 25010 — Product Quality Model

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 25010 |
| **Title** | Systems and Software Engineering — Product Quality Model |
| **Category** | Software Quality |
| **EoS Alignment** | EoS addresses all eight quality characteristics: **Functional suitability** (41 product profiles, 33 HAL interfaces), **Performance efficiency** (bounded IPC queues, priority lanes), **Compatibility** (POSIX/VxWorks/Linux compatibility layers), **Usability** (EoSDesign GUI, eAppSuite cross-platform UI), **Reliability** (watchdog, crypto verification, health monitoring), **Security** (HMAC, capability-based auth, keyring), **Maintainability** (modular architecture, semantic versioning), **Portability** (cross-platform builds for Linux/Windows/macOS, cross-compilation for AArch64/ARM/RISC-V). |
| **Relevant Repos** | `eos`, `eipc`, `eAppSuite`, `eMobile-Apps`, `EoSDesign`, `eosim` |

### ISO/IEC 25040 — Quality Evaluation Process

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 25040 |
| **Title** | Systems and Software Engineering — Quality Evaluation Process |
| **Category** | Software Quality |
| **EoS Alignment** | Quality evaluation is implemented through multi-tier automated testing: unit tests (per-repo), integration tests (QEMU boot sanity across x86_64/aarch64/riscv64), simulation tests (eosim product-specific validation), and nightly/weekly regression runs. Test results and coverage metrics are published as CI artifacts. |
| **Relevant Repos** | All repositories with test suites |

---

## 4. Information Security

### ISO/IEC 27001 — Information Security Management Systems

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 27001 |
| **Title** | Information Security Management Systems — Requirements |
| **Category** | Information Security |
| **EoS Alignment** | EoS implements security controls at every layer: secure boot chain (`eboot`), cryptographic services (SHA-256/512, AES, RSA, ECC in `eos`), access control lists, keystore management, audit logging, and integrity verification. The `eipc` framework provides authentication, capability-based authorization, HMAC integrity, and replay protection. All repos have `SECURITY.md` with vulnerability disclosure processes. Weekly CI runs include dependency security audits. |
| **Relevant Repos** | `eos`, `eboot`, `eipc`, `eos-sdk`, all repos (SECURITY.md) |

### ISO/IEC 15408 — Common Criteria for IT Security Evaluation

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 15408 |
| **Title** | Information Technology — Security Techniques — Evaluation Criteria for IT Security |
| **Category** | Security Evaluation |
| **EoS Alignment** | EoS security architecture maps to Common Criteria concepts: Security Functional Requirements (SFRs) are implemented in `eos` security services (keystore, ACL, secure boot, audit), `eipc` security modules (auth, capability, integrity, replay, keyring), and `eboot` verified boot. Security Assurance Requirements (SARs) are addressed through code review, automated testing, and formal documentation. Target of Evaluation (TOE) can be defined per product profile. |
| **Relevant Repos** | `eos`, `eboot`, `eipc`, `eos-sdk` |

### ISO/IEC 20243 — Open Trusted Technology Provider Standard (O-TTPS)

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 20243 |
| **Title** | Information Technology — Open Trusted Technology Provider Standard (O-TTPS) |
| **Category** | Supply Chain Security |
| **EoS Alignment** | EoS follows O-TTPS principles: all source code is publicly available on GitHub, builds are reproducible via CI/CD, release artifacts include SHA256 checksums, dependencies are audited, and the supply chain from source to binary is fully transparent. The `ebuild` and `ebuild-tool` repos provide the trusted build infrastructure. SPDX license identifiers are used throughout. |
| **Relevant Repos** | `ebuild`, `ebuild-tool`, `.github`, all repositories |

---

## 5. Risk Management

### ISO 31000 — Risk Management

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO 31000 |
| **Title** | Risk Management — Guidelines |
| **Category** | Risk Management |
| **EoS Alignment** | Risk is managed through multiple mechanisms: `SECURITY.md` files define vulnerability response processes, `eboot` implements verified boot to mitigate firmware tampering, `eos` watchdog services address system hang risks, `eipc` policy engine classifies actions into safe/controlled/restricted tiers, and `eosim` enables pre-deployment risk assessment through simulation. Product profiles define safety-critical requirements per industry vertical. |
| **Relevant Repos** | `eos`, `eboot`, `eipc`, `eosim`, all repos (SECURITY.md) |

---

## 6. Vulnerability Handling

### ISO/IEC 30111 — Vulnerability Handling Processes

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 30111 |
| **Title** | Information Technology — Security Techniques — Vulnerability Handling Processes |
| **Category** | Vulnerability Management |
| **EoS Alignment** | Each EoS repo contains `SECURITY.md` defining the vulnerability handling process: report to security@embeddedos.org → triage within 48 hours → CVE assignment if applicable → fix development → advisory publication → coordinated disclosure. Weekly CI runs scan for known vulnerabilities in dependencies. |
| **Relevant Repos** | All repositories |

### ISO/IEC 29147 — Vulnerability Disclosure

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 29147 |
| **Title** | Information Technology — Security Techniques — Vulnerability Disclosure |
| **Category** | Vulnerability Disclosure |
| **EoS Alignment** | Coordinated vulnerability disclosure is documented in every repo's `SECURITY.md`. The process follows: private report → acknowledgment → coordinated fix → public advisory. Security contacts and expected response times are clearly published. GitHub Security Advisories are used for CVE tracking. |
| **Relevant Repos** | All repositories |

---

## 7. Testing

### ISO/IEC/IEEE 29119 — Software and Systems Engineering — Software Testing

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC/IEEE 29119 |
| **Title** | Software and Systems Engineering — Software Testing |
| **Category** | Testing |
| **EoS Alignment** | EoS implements a comprehensive test strategy across five levels: **Unit testing** (pytest, go test, JUnit, dart test per repo), **Integration testing** (cross-module tests), **System testing** (QEMU boot sanity across 3 architectures), **Simulation testing** (eosim product-specific validation with 20+ platform definitions), and **Acceptance testing** (CI gate on all PRs). Test infrastructure includes nightly and weekly regression suites, coverage reporting, and test artifact archival. |
| **Relevant Repos** | All repositories |

---

## 8. Privacy

### ISO/IEC 27701 — Privacy Information Management

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 27701 |
| **Title** | Security Techniques — Extension to ISO/IEC 27001 and ISO/IEC 27002 for Privacy Information Management |
| **Category** | Privacy |
| **EoS Alignment** | Privacy is addressed through: minimal data collection in `eipc` audit logs (configurable retention), capability-based access control limiting data exposure, secure storage services in `eos` for personal data protection, and privacy-aware UI design guidelines in `EoSDesign`. The `eMobile-Apps` permission system (`emobile_platform` package) enforces explicit consent for sensor and filesystem access. |
| **Relevant Repos** | `eos`, `eipc`, `eMobile-Apps`, `EoSDesign` |

---

## 9. Data Security

### ISO/IEC 27040 — Storage Security

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 27040 |
| **Title** | Information Technology — Security Techniques — Storage Security |
| **Category** | Data Security |
| **EoS Alignment** | EoS provides secure storage through: AES-encrypted secure storage in `eos` OS services, keystore management with hardware-backed options, Flash HAL with wear-leveling and integrity checks, SDIO interface for removable storage, and RAID management in datacenter profiles. The `eipc` keyring service manages cryptographic key lifecycle including rotation and cleanup. |
| **Relevant Repos** | `eos`, `eipc`, `eos-sdk` |

---

## 10. Cloud Computing

### ISO/IEC 17788 — Cloud Computing — Overview and Vocabulary

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 17788 |
| **Title** | Information Technology — Cloud Computing — Overview and Vocabulary |
| **Category** | Cloud Computing |
| **EoS Alignment** | EoS supports cloud-edge computing patterns through: datacenter product profiles (virtualization, BMC/IPMI, load balancer, routing, QoS, failover), Ethernet/WiFi/Cellular HAL interfaces for cloud connectivity, and `eipc` for secure communication between edge devices and cloud services. The `eosim` simulator can model cloud-connected embedded systems. |
| **Relevant Repos** | `eos`, `eipc`, `eosim`, `eos-platform` |

### ISO/IEC 17789 — Cloud Computing — Reference Architecture

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 17789 |
| **Title** | Information Technology — Cloud Computing — Reference Architecture |
| **Category** | Cloud Computing |
| **EoS Alignment** | EoS datacenter profiles implement cloud reference architecture components: compute virtualization, storage management (RAID), network services (routing, QoS, load balancing), thermal management, and failover mechanisms. The `eos-platform` repo provides platform abstraction enabling cloud deployment. |
| **Relevant Repos** | `eos`, `eos-platform` |

---

## 11. Usability

### ISO 9241 — Ergonomics of Human-System Interaction

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO 9241 |
| **Title** | Ergonomics of Human-System Interaction |
| **Category** | Usability |
| **EoS Alignment** | Usability principles from ISO 9241 are applied in: `EoSDesign` (2D/3D design tool with color picker, layers panel, properties panel, toolbar, viewport), `eAppSuite` (cross-platform apps with AppTheme, AppColors, AppTypography, responsive layout, adaptive scaffold), `eMobile-Apps` (Flutter apps with emobile_ui theme system, responsive layout), and `eosim` (simulator GUI with peripheral panels, memory view, CPU dashboard, UART terminal, 3D viewer). HMI product profiles address automotive/industrial display ergonomics. |
| **Relevant Repos** | `EoSDesign`, `eAppSuite`, `eMobile-Apps`, `eosim`, `eos` (HMI profiles) |

---

## 12. Innovation

### ISO 56002 — Innovation Management

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO 56002 |
| **Title** | Innovation Management — Innovation Management System — Guidance |
| **Category** | Innovation |
| **EoS Alignment** | EoS demonstrates systematic innovation through: AI integration (`eai` for embedded AI inference, `EoSDesign` AI-assisted design), neural interface support (`eni`), comprehensive simulation (`eosim` with 20+ platform definitions and 3D visualization), and cross-platform reach (desktop, mobile, web, embedded). The open-source model enables community-driven innovation. Product profiles span 41 categories across automotive, medical, aerospace, consumer, industrial, networking, and financial domains. |
| **Relevant Repos** | `eai`, `eni`, `eosim`, `EoSDesign`, all repositories |

---

## 13. Quality Management

### ISO 9001 — Quality Management Systems

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO 9001 |
| **Title** | Quality Management Systems — Requirements |
| **Category** | Quality Management |
| **EoS Alignment** | EoS quality management is implemented through: documented processes (CONTRIBUTING.md, architecture docs), automated quality gates (CI/CD with lint, test, build verification), continuous improvement (CHANGELOG tracking, semantic versioning), customer focus (41 product profiles addressing specific market needs), evidence-based decision making (test coverage metrics, build pass rates), and relationship management (CODE_OF_CONDUCT.md, open-source community governance). |
| **Relevant Repos** | All repositories |

---

## 14. Functional Safety

### IEC 61508 — Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems

| Attribute | Detail |
|-----------|--------|
| **Standard** | IEC 61508 |
| **Title** | Functional Safety of E/E/PE Safety-Related Systems |
| **Category** | Functional Safety |
| **EoS Alignment** | EoS supports safety-critical applications through: watchdog timer HAL and OS service, secure boot chain (`eboot`), cryptographic integrity verification, audit trail logging, hardware abstraction for safety-relevant peripherals (CAN bus, motor control with PID), and product profiles for safety-critical industries (automotive, medical, aerospace, industrial). The `eosim` simulator enables safety validation prior to deployment. |
| **Relevant Repos** | `eos`, `eboot`, `eosim`, `eos-platform` |

### ISO 26262 — Road Vehicles — Functional Safety

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO 26262 |
| **Title** | Road Vehicles — Functional Safety |
| **Category** | Automotive Safety |
| **EoS Alignment** | Automotive product profiles in `eos/products/` address ISO 26262 requirements: CAN bus communication, motor control, sensor fusion (IMU, radar, GNSS), real-time constraints (priority-based scheduling), watchdog monitoring, and diagnostic services. The `eosim` vehicle simulator provides HIL-ready validation. ASIL decomposition can be mapped to EoS module boundaries. |
| **Relevant Repos** | `eos`, `eboot`, `eosim`, `eipc`, `eos-platform` |

### DO-178C — Software Considerations in Airborne Systems and Equipment Certification

| Attribute | Detail |
|-----------|--------|
| **Standard** | DO-178C |
| **Title** | Software Considerations in Airborne Systems and Equipment Certification |
| **Category** | Aerospace Safety |
| **EoS Alignment** | Aerospace product profiles address DO-178C concepts: traceable requirements (product profile headers), deterministic execution (RTOS platform backend), verified boot (`eboot`), integrity monitoring (watchdog, CRC), and comprehensive testing (unit + integration + QEMU + simulation). The `eosim` aircraft simulator models avionics scenarios. Design Assurance Levels (DAL A–E) can be mapped to test rigor levels. |
| **Relevant Repos** | `eos`, `eboot`, `eosim`, `eos-platform` |

### EN 50128 — Railway Applications — Communication, Signalling and Processing Systems

| Attribute | Detail |
|-----------|--------|
| **Standard** | EN 50128 |
| **Title** | Railway Applications — Software for Railway Control and Protection Systems |
| **Category** | Railway Safety |
| **EoS Alignment** | EoS supports railway applications through: deterministic real-time execution, CAN/Ethernet communication, safety monitoring (watchdog, integrity checks), secure boot, and comprehensive verification. Product profiles can be configured for SIL 0–4 requirements. Formal verification artifacts can be generated through `eosim` simulation traces. |
| **Relevant Repos** | `eos`, `eboot`, `eosim`, `eipc` |

---

## 15. Compliance Matrix

| Standard | Category | EoS Repos | Status |
|----------|----------|-----------|--------|
| ISO/IEC/IEEE 15288:2023 | Systems Engineering | eos, eboot, eipc, eai, eni, ebuild, eosim, eos-platform, EoSDesign | ✅ Aligned |
| ISO/IEC 12207 | Software Engineering | All | ✅ Aligned |
| ISO/IEC/IEEE 42010 | Architecture | .github, embeddedos-org.github.io, eipc, eAppSuite, eMobile-Apps, EoSDesign | ✅ Aligned |
| ISO/IEC/IEEE 828 | Configuration Mgmt | All | ✅ Aligned |
| ISO/IEC 330xx | Process Assessment | .github, All with CI/CD | ✅ Aligned |
| ISO/IEC 25000 (SQuaRE) | Software Quality | All | ✅ Aligned |
| ISO/IEC 25010 | Product Quality | eos, eipc, eAppSuite, eMobile-Apps, EoSDesign, eosim | ✅ Aligned |
| ISO/IEC 25040 | Quality Evaluation | All with tests | ✅ Aligned |
| ISO/IEC 27001 | Information Security | eos, eboot, eipc, eos-sdk, All | ✅ Aligned |
| ISO/IEC 15408 | Common Criteria | eos, eboot, eipc, eos-sdk | ✅ Aligned |
| ISO/IEC 20243 (O-TTPS) | Supply Chain | ebuild, ebuild-tool, .github, All | ✅ Aligned |
| ISO 31000 | Risk Management | eos, eboot, eipc, eosim, All | ✅ Aligned |
| ISO/IEC 30111 | Vulnerability Handling | All | ✅ Aligned |
| ISO/IEC 29147 | Vulnerability Disclosure | All | ✅ Aligned |
| ISO/IEC/IEEE 29119 | Testing | All | ✅ Aligned |
| ISO/IEC 27701 | Privacy | eos, eipc, eMobile-Apps, EoSDesign | ✅ Aligned |
| ISO/IEC 27040 | Storage Security | eos, eipc, eos-sdk | ✅ Aligned |
| ISO/IEC 17788 | Cloud Overview | eos, eipc, eosim, eos-platform | ✅ Aligned |
| ISO/IEC 17789 | Cloud Architecture | eos, eos-platform | ✅ Aligned |
| ISO 9241 | Usability | EoSDesign, eAppSuite, eMobile-Apps, eosim | ✅ Aligned |
| ISO 56002 | Innovation | eai, eni, eosim, EoSDesign, All | ✅ Aligned |
| ISO 9001 | Quality Management | All | ✅ Aligned |
| IEC 61508 | Functional Safety | eos, eboot, eosim, eos-platform | ✅ Aligned |
| ISO 26262 | Automotive Safety | eos, eboot, eosim, eipc, eos-platform | ✅ Aligned |
| DO-178C | Aerospace Safety | eos, eboot, eosim, eos-platform | ✅ Aligned |
| EN 50128 | Railway Safety | eos, eboot, eosim, eipc | ✅ Aligned |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial standards alignment document |
