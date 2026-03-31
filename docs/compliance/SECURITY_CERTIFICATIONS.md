# EoS Security Certifications

> **Document**: SECURITY_CERTIFICATIONS.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document covers security certification standards applicable to EoS, mapping each standard to specific EoS security features, crypto modules, and secure infrastructure components.

---

## Table of Contents

1. [Overview](#1-overview)
2. [ISO/IEC 27001 — ISMS](#2-isoiec-27001--isms)
3. [ISO/IEC 15408 — Common Criteria](#3-isoiec-15408--common-criteria)
4. [FIPS 140-3 — Cryptographic Modules](#4-fips-140-3--cryptographic-modules)
5. [ISO/IEC 30111 — Vulnerability Handling](#5-isoiec-30111--vulnerability-handling)
6. [ISO/IEC 29147 — Vulnerability Disclosure](#6-isoiec-29147--vulnerability-disclosure)
7. [ISO/IEC 27701 — Privacy Management](#7-isoiec-27701--privacy-management)
8. [ISO/IEC 27040 — Storage Security](#8-isoiec-27040--storage-security)
9. [EoS Security Architecture](#9-eos-security-architecture)
10. [Compliance Matrix](#10-compliance-matrix)

---

## 1. Overview

EoS implements defense-in-depth security across the entire stack — from secure boot to application-level access controls. This document maps international security standards to EoS's cryptographic module, authentication mechanisms, integrity verification, and privacy features.

### EoS Security Stack

```
┌─────────────────────────────────────────────┐
│  Application Layer — ACL, SELinux policies   │
├─────────────────────────────────────────────┤
│  Service Layer — HMAC auth (eipc), keystore  │
├─────────────────────────────────────────────┤
│  Kernel Layer — MPU isolation, IMA, dm-verity│
├─────────────────────────────────────────────┤
│  Boot Layer — Secure boot (eboot), RSA/ECC   │
├─────────────────────────────────────────────┤
│  Crypto Module — SHA-256, AES-256, RSA/ECC   │
└─────────────────────────────────────────────┘
```

---

## 2. ISO/IEC 27001 — ISMS

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 27001:2022 |
| **Full Name** | Information security, cybersecurity and privacy protection — Information security management systems — Requirements |
| **Scope** | Requirements for establishing, implementing, maintaining, and continually improving an ISMS |

### EoS ISMS Alignment

| ISO 27001 Clause | Requirement | EoS Implementation |
|-------------------|-------------|---------------------|
| **A.5** | Information security policies | ✅ `SECURITY.md` in every repo, org-level security policy |
| **A.6** | Organization of information security | ✅ Maintainer roles, code owners, security response team |
| **A.7** | Human resource security | ✅ `CONTRIBUTING.md` with security guidelines |
| **A.8** | Asset management | ✅ SBOM tracks all software assets |
| **A.9** | Access control | ✅ GitHub org roles, branch protection, ACL in kernel |
| **A.10** | Cryptography | ✅ Crypto module (SHA-256, AES-256, RSA/ECC) |
| **A.11** | Physical and environmental | N/A — software project |
| **A.12** | Operations security | ✅ CI/CD security scanning, dependency auditing |
| **A.13** | Communications security | ✅ TLS in `eipc`, HMAC message authentication |
| **A.14** | System acquisition/development | ✅ Secure development lifecycle, code review |
| **A.15** | Supplier relationships | ✅ `SUPPLY_CHAIN.md`, dependency auditing |
| **A.16** | Incident management | ✅ 48-hour response SLA, GitHub Security Advisories |
| **A.17** | Business continuity | ✅ Multi-maintainer structure, bus factor mitigation |
| **A.18** | Compliance | ✅ This compliance document suite |

---

## 3. ISO/IEC 15408 — Common Criteria

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 15408:2022 (parts 1–3) |
| **Full Name** | Information technology — Security techniques — Evaluation criteria for IT security |
| **Parts** | Part 1: Introduction, Part 2: Security functional components, Part 3: Security assurance components |

### Evaluation Assurance Levels (EAL)

| EAL | Name | Description | EoS Applicability |
|:---:|------|-------------|:-----------------:|
| **EAL1** | Functionally tested | Basic independent testing | ✅ Supported |
| **EAL2** | Structurally tested | Developer testing + independent analysis | ✅ Supported |
| **EAL3** | Methodically tested and checked | Systematic testing, design analysis | ✅ Supported |
| **EAL4** | Methodically designed, tested, reviewed | Independent vulnerability analysis | 🔶 Partial |
| **EAL5** | Semi-formally designed and tested | Semi-formal design, covert channel analysis | 📋 Planned |
| **EAL6** | Semi-formally verified design, tested | Structured development, modular design | 📋 Planned |
| **EAL7** | Formally verified design and tested | Formal model, complete independent testing | 📋 Planned |

### Security Functional Requirements (SFR) — EoS Mapping

| SFR Class | Requirement | EoS Implementation |
|-----------|-------------|---------------------|
| **FAU** (Audit) | Security audit data generation | ✅ Audit logging with HMAC integrity |
| **FCS** (Crypto) | Cryptographic key management | ✅ Keystore, RSA/ECC key generation |
| **FCS** (Crypto) | Cryptographic operation | ✅ SHA-256, AES-256-CBC, HMAC-SHA256 |
| **FDP** (Data Protection) | Access control policy | ✅ ACL-based access control, SELinux |
| **FIA** (Auth) | User authentication | ✅ HMAC-based identity in `eipc` |
| **FMT** (Mgmt) | Security management functions | ✅ Kernel privilege levels, capability model |
| **FPT** (Protection) | TSF self-protection | ✅ MPU isolation, secure boot chain |
| **FRU** (Resource) | Resource utilization | ✅ Watchdog, stack guards, memory limits |
| **FTP** (Trusted Path) | Trusted communication | ✅ TLS transport in `eipc`, HMAC auth |

---

## 4. FIPS 140-3 — Cryptographic Modules

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | FIPS 140-3 (NIST) |
| **Full Name** | Security Requirements for Cryptographic Modules |
| **Levels** | Level 1 (software), Level 2 (tamper evidence), Level 3 (tamper resistance), Level 4 (environmental) |

### FIPS 140-3 Security Levels — EoS Mapping

| Level | Requirement | EoS Status |
|:-----:|-------------|:----------:|
| **Level 1** | Approved algorithms, no physical security | ✅ Supported |
| **Level 2** | Tamper-evident coatings, role-based auth | 🔶 Partial (role-based) |
| **Level 3** | Tamper resistance, identity-based auth | 📋 Planned |
| **Level 4** | Environmental failure protection | 📋 Planned |

### EoS Cryptographic Module

| Algorithm | Type | Standard | Implementation | Repo |
|-----------|------|----------|----------------|------|
| **SHA-256** | Hash | FIPS 180-4 | Software | `eos` (crypto module) |
| **AES-256-CBC** | Symmetric cipher | FIPS 197 | Software | `eos` (crypto module) |
| **HMAC-SHA256** | MAC | FIPS 198-1 | Software | `eipc` (auth module) |
| **RSA-2048** | Asymmetric cipher | FIPS 186-5 | Software | `eboot` (signature verification) |
| **ECDSA P-256** | Digital signature | FIPS 186-5 | Software | `eboot` (signature verification) |
| **ECDH P-256** | Key agreement | SP 800-56A | Software | `eipc` (TLS key exchange) |
| **AES-256-GCM** | AEAD cipher | SP 800-38D | Software | `eipc` (TLS record protection) |

### Key Management

| Function | Implementation | Repo |
|----------|----------------|------|
| Key generation | CSPRNG-seeded RSA/ECC key pairs | `eos`, `eboot` |
| Key storage | Encrypted keystore partition | `eos` |
| Key rotation | Configurable rotation policy | `eos-platform` |
| Key destruction | Secure zeroization on revocation | `eos` |

---

## 5. ISO/IEC 30111 — Vulnerability Handling

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 30111:2019 |
| **Full Name** | Information technology — Security techniques — Vulnerability handling processes |
| **Scope** | Vendor-side processes for receiving, investigating, and resolving vulnerability reports |

### EoS Vulnerability Handling Process

| ISO 30111 Phase | EoS Implementation |
|-----------------|---------------------|
| **Preparation** | `SECURITY.md` with contact info, PGP key, scope definition |
| **Receipt** | Private security email, GitHub Security Advisory (GHSA) |
| **Verification** | Maintainer triage within 48 hours, reproduction in eosim/QEMU |
| **Remediation** | Patch development, private branch, security review |
| **Disclosure** | Coordinated disclosure with reporter, CVE assignment |
| **Post-disclosure** | Public advisory, CHANGELOG entry, SBOM update |

### Response SLAs

| Severity | Initial Response | Fix Target | Disclosure |
|:--------:|:----------------:|:----------:|:----------:|
| Critical | 24 hours | 7 days | Coordinated |
| High | 48 hours | 14 days | Coordinated |
| Medium | 72 hours | 30 days | Coordinated |
| Low | 5 business days | Next release | Public |

---

## 6. ISO/IEC 29147 — Vulnerability Disclosure

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 29147:2018 |
| **Full Name** | Information technology — Security techniques — Vulnerability disclosure |
| **Scope** | Guidelines for vendors on receiving and publishing vulnerability information |

### EoS Disclosure Policy

| Requirement | EoS Implementation |
|-------------|---------------------|
| Public reporting channel | ✅ `SECURITY.md` in every repo with email address |
| Encrypted communication | ✅ PGP key published for encrypted reports |
| Acknowledgment timeline | ✅ 48-hour initial response |
| Disclosure coordination | ✅ 90-day coordinated disclosure window |
| CVE assignment | ✅ CNA or MITRE CVE request process |
| Advisory publication | ✅ GitHub Security Advisory (GHSA) |
| Credit to reporters | ✅ Named credit in advisory unless declined |
| Fix availability | ✅ Patch release before public disclosure |

---

## 7. ISO/IEC 27701 — Privacy Management

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 27701:2019 |
| **Full Name** | Security techniques — Extension to ISO/IEC 27001 and ISO/IEC 27002 for privacy information management |
| **Scope** | Privacy-specific requirements and guidance for PII processing |

### EoS Privacy Alignment

| Privacy Principle | EoS Implementation |
|-------------------|---------------------|
| **Data minimization** | ✅ No PII collected by kernel or services by default |
| **Purpose limitation** | ✅ Telemetry (if enabled) used only for diagnostics |
| **Consent** | ✅ Telemetry is opt-in only, disabled by default |
| **Transparency** | ✅ Privacy policy documented, data flows published |
| **Confidentiality** | ✅ Encrypted storage (keystore), TLS transport |
| **Integrity** | ✅ HMAC-signed data, dm-verity filesystem |
| **Accountability** | ✅ Audit logging of data access events |

### EoS Privacy by Design

| Feature | Description | Repo |
|---------|-------------|------|
| Local inference | `eai` runs ML models on-device, no cloud PII transfer | `eai` |
| Encrypted keystore | Credentials stored in encrypted partition | `eos` |
| Telemetry opt-in | Diagnostic telemetry disabled by default | `eos-platform` |
| Secure IPC | `eipc` HMAC prevents unauthorized data access | `eipc` |
| Audit trail | Tamper-evident logs of security-relevant events | `eos` |

---

## 8. ISO/IEC 27040 — Storage Security

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO/IEC 27040:2015 |
| **Full Name** | Information technology — Security techniques — Storage security |
| **Scope** | Security for data storage systems, media, and infrastructure |

### EoS Storage Security Features

| Feature | Description | Standard Alignment |
|---------|-------------|-------------------|
| **dm-verity** | Block-level integrity verification for read-only filesystems | ISO 27040 §7.4 (integrity) |
| **IMA** | Integrity Measurement Architecture — runtime file integrity | ISO 27040 §7.4 (integrity) |
| **Encrypted partitions** | LUKS/dm-crypt for user data partitions | ISO 27040 §7.5 (confidentiality) |
| **Secure erase** | NIST 800-88 compliant media sanitization | ISO 27040 §7.7 (disposal) |
| **Keystore** | Hardware-backed key storage (when available) | ISO 27040 §7.6 (key management) |
| **Flash wear leveling** | Secure awareness of wear-leveled flash storage | ISO 27040 §7.3 (media) |

### Storage Layout Security

| Partition | Protection | Write Access |
|-----------|------------|:------------:|
| Boot (eboot) | Signed + verified | Read-only |
| Kernel | dm-verity protected | Read-only |
| Root filesystem | dm-verity protected | Read-only |
| User data | Encrypted (LUKS) | Read-write |
| Keystore | Encrypted + ACL | Privileged only |
| Logs | HMAC-signed | Append-only |

---

## 9. EoS Security Architecture

### Secure Boot Chain

```
ROM Bootloader → eboot (RSA/ECC verified) → Kernel (hash verified) → Services → Apps
     │                    │                        │                    │
     └── HW root of trust └── Signature check      └── dm-verity       └── ACL/SELinux
```

### Authentication and Authorization

| Mechanism | Layer | Description | Repo |
|-----------|-------|-------------|------|
| HMAC-SHA256 | IPC | Message authentication between services | `eipc` |
| ACL | Kernel | Capability-based access control | `eos` |
| SELinux | OS | Mandatory access control policies | `eos-platform` |
| TLS 1.3 | Network | Encrypted communication channels | `eipc` |
| Secure boot | Boot | Cryptographic chain of trust | `eboot` |

### Integrity Verification

| Mechanism | Scope | Description |
|-----------|-------|-------------|
| dm-verity | Filesystem | Block-level hash tree for read-only partitions |
| IMA | Runtime | File hash verification before execution |
| HMAC | IPC messages | Per-message integrity and authenticity |
| Secure boot | Boot chain | Signature verification of each boot stage |
| SBOM | Supply chain | Provenance verification of all components |

---

## 10. Compliance Matrix

| Standard | Requirement | EoS Status |
|----------|-------------|------------|
| ISO/IEC 27001 | Information security management system | ✅ Aligned |
| ISO/IEC 27001 A.9 | Access control | ✅ ACL + SELinux |
| ISO/IEC 27001 A.10 | Cryptography | ✅ SHA-256, AES-256, RSA/ECC |
| ISO/IEC 27001 A.13 | Communications security | ✅ TLS + HMAC |
| ISO/IEC 27001 A.16 | Incident management | ✅ 48-hour response SLA |
| ISO/IEC 15408 EAL1–3 | Common Criteria evaluation | ✅ Supported |
| ISO/IEC 15408 EAL4 | Independent vulnerability analysis | 🔶 Partial |
| ISO/IEC 15408 EAL5–7 | Semi-formal/formal verification | 📋 Planned |
| FIPS 140-3 Level 1 | Approved crypto algorithms | ✅ Supported |
| FIPS 140-3 Level 2 | Tamper evidence + role-based auth | 🔶 Partial |
| FIPS 140-3 Level 3–4 | Tamper resistance + environmental | 📋 Planned |
| ISO/IEC 30111 | Vulnerability handling process | ✅ Implemented |
| ISO/IEC 29147 | Vulnerability disclosure policy | ✅ Implemented |
| ISO/IEC 27701 | Privacy information management | ✅ Aligned |
| ISO/IEC 27040 | Storage security | ✅ Aligned |
| Crypto module — SHA-256 | FIPS 180-4 hash | ✅ Implemented |
| Crypto module — AES-256 | FIPS 197 cipher | ✅ Implemented |
| Crypto module — RSA/ECC | FIPS 186-5 signatures | ✅ Implemented |
| Secure boot chain | eboot → kernel → apps | ✅ Implemented |
| HMAC authentication | eipc message integrity | ✅ Implemented |
| Keystore | Encrypted credential storage | ✅ Implemented |
| ACL + SELinux | Access control enforcement | ✅ Implemented |
| dm-verity | Filesystem integrity | ✅ Implemented |
| IMA | Runtime integrity measurement | 🔶 Partial |

**Legend**: ✅ Aligned/Implemented | 🔶 Partial | 📋 Planned

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial security certifications document |
# EoS Security Certifications

> **Document**: SECURITY_CERTIFICATIONS.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document maps EoS security features to FIPS 140-3, Common Criteria (ISO/IEC 15408), and ISO/IEC 27001.

---

## Table of Contents

1. [Overview](#1-overview)
2. [FIPS 140-3](#2-fips-140-3)
3. [Common Criteria (ISO/IEC 15408)](#3-common-criteria-isoiec-15408)
4. [ISO/IEC 27001](#4-isoiec-27001)
5. [EoS Security Architecture](#5-eos-security-architecture)
6. [Certification Roadmap](#6-certification-roadmap)

---

## 1. Overview

### Security-Relevant EoS Components

| Component | Repo | Security Functions |
|-----------|------|--------------------|
| **eos Crypto Services** | `eos` | SHA-256/512, AES-128/256, RSA-2048/4096, ECC P-256/P-384, CRC-32 |
| **eos Keystore** | `eos` | Secure key storage, key lifecycle management |
| **eos ACL** | `eos` | Access control lists, permission enforcement |
| **eos Secure Boot** | `eos` | Boot-time integrity verification |
| **eos Audit** | `eos` | Security event logging, tamper-evident audit trail |
| **eboot Verified Boot** | `eboot` | Multi-stage boot verification, firmware signature validation |
| **eipc Auth** | `eipc` | Peer authentication, session management |
| **eipc Capability** | `eipc` | Fine-grained authorization, runtime grant/revoke |
| **eipc Integrity** | `eipc` | HMAC-SHA256 message signing and verification |
| **eipc Replay** | `eipc` | Sliding-window sequence number replay detection |
| **eipc Keyring** | `eipc` | Key generation, rotation, expiry, cleanup |

---

## 2. FIPS 140-3

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Full Title** | Security Requirements for Cryptographic Modules |
| **Issuer** | NIST (National Institute of Standards and Technology) |
| **Levels** | Level 1 (basic) through Level 4 (highest physical security) |
| **Supersedes** | FIPS 140-2 |
| **ISO Equivalent** | ISO/IEC 19790:2012 |

### EoS Cryptographic Module Mapping

| FIPS 140-3 Area | EoS Implementation | Repo |
|-----------------|---------------------|------|
| **Symmetric encryption** | AES-128, AES-256 (CBC, CTR, GCM modes) | `eos` |
| **Asymmetric encryption** | RSA-2048, RSA-4096 | `eos` |
| **Digital signatures** | RSA-PSS, ECDSA (P-256, P-384) | `eos`, `eboot` |
| **Hash functions** | SHA-256, SHA-512 | `eos`, `eipc` |
| **Message authentication** | HMAC-SHA256 | `eipc` |
| **Key generation** | CSPRNG-based key generation | `eipc` (keyring) |
| **Key management** | Key storage, rotation, expiry, revocation | `eos` (keystore), `eipc` (keyring) |
| **Random number generation** | Platform RNG with entropy pool | `eos` |
| **Integrity verification** | CRC-32, SHA-256 firmware hash | `eos`, `eboot` |

### FIPS 140-3 Section Alignment

| Section | Requirement | EoS Status |
|---------|-------------|------------|
| §7.1 | Cryptographic module specification | ✅ Documented API in `eos/include/eos/services/crypto.h` |
| §7.2 | Cryptographic module interfaces | ✅ Defined C API with clear input/output boundaries |
| §7.3 | Roles, services, and authentication | ✅ ACL-based roles, capability-based auth |
| §7.4 | Software/firmware security | ✅ Verified boot, integrity checks |
| §7.5 | Operational environment | ✅ RTOS and Linux platform backends |
| §7.6 | Physical security | 📋 Hardware-dependent, documented in product profiles |
| §7.7 | Non-invasive security | 📋 Side-channel mitigation planned |
| §7.8 | Sensitive security parameter management | ✅ Keystore with ACL, keyring with rotation |
| §7.9 | Self-tests | ✅ Power-on integrity check via `eboot` |
| §7.10 | Life-cycle assurance | ✅ CI/CD, version control, secure build pipeline |
| §7.11 | Mitigation of other attacks | 🔄 Replay protection, timing-safe comparison |

### Target FIPS 140-3 Level

| EoS Module | Target Level | Rationale |
|------------|:------------:|-----------|
| `eos` crypto services | Level 1 | Software-only cryptographic module |
| `eboot` verified boot | Level 2 | Tamper-evident boot chain |
| `eipc` security | Level 1 | Software-only integrity and auth |

---

## 3. Common Criteria (ISO/IEC 15408)

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Full Title** | Information Technology — Security Techniques — Evaluation Criteria for IT Security |
| **Parts** | Part 1: Introduction, Part 2: Security Functional Components, Part 3: Security Assurance Components |
| **Evaluation Levels** | EAL1 (functionally tested) through EAL7 (formally verified) |

### Security Target (ST) Outline for EoS

#### Target of Evaluation (TOE)

The EoS TOE comprises the embedded operating system kernel (`eos`), bootloader (`eboot`), and IPC framework (`eipc`) running on supported hardware platforms (AArch64, ARM, RISC-V, x86_64).

#### Security Functional Requirements (SFRs)

| SFR Class | SFR Component | EoS Implementation |
|-----------|---------------|---------------------|
| **FAU** (Audit) | FAU_GEN.1 — Audit data generation | `eos` audit service, `eipc` audit logger |
| **FAU** | FAU_SAR.1 — Audit review | JSON-line audit logs, searchable |
| **FCS** (Crypto) | FCS_COP.1 — Cryptographic operation | AES, RSA, ECC, SHA, HMAC in `eos` |
| **FCS** | FCS_CKM.1 — Key generation | `eipc` keyring CSPRNG generation |
| **FCS** | FCS_CKM.4 — Key destruction | `eipc` keyring cleanup, `eos` keystore revocation |
| **FDP** (Data Protection) | FDP_ACC.1 — Access control | `eos` ACL, `eipc` capability checker |
| **FDP** | FDP_IFC.1 — Information flow control | `eipc` policy engine (safe/controlled/restricted) |
| **FIA** (Auth) | FIA_UAU.2 — User authentication | `eipc` peer authentication with session tokens |
| **FIA** | FIA_UID.2 — User identification | `eipc` service registry with ServiceID |
| **FMT** (Management) | FMT_MSA.1 — Management of security attributes | Runtime capability grant/revoke |
| **FPT** (Protection) | FPT_FLS.1 — Failure with preservation of secure state | Watchdog timeout → safe state |
| **FPT** | FPT_TST.1 — TSF self test | `eboot` firmware integrity verification |
| **FTA** (Access) | FTA_SSL.3 — TSF-initiated termination | Session timeout, replay detection |

#### Security Assurance Requirements (SARs)

| SAR Class | Component | EoS Evidence |
|-----------|-----------|-------------|
| **ADV** (Development) | ADV_ARC.1 — Security architecture | Architecture docs, module diagrams |
| **ADV** | ADV_FSP.1 — Functional specification | C header files (`.h`) as formal API |
| **ADV** | ADV_TDS.1 — TOE design | README architecture sections |
| **AGD** (Guidance) | AGD_OPE.1 — Operational user guidance | Getting-started guides, API docs |
| **ALC** (Life-cycle) | ALC_CMC.1 — CM capabilities | Git + SemVer + CI/CD |
| **ALC** | ALC_CMS.1 — CM scope | All source in Git |
| **ATE** (Tests) | ATE_COV.1 — Evidence of coverage | CI coverage reports |
| **ATE** | ATE_FUN.1 — Functional testing | Unit + QEMU + eosim tests |
| **AVA** (Vulnerability) | AVA_VAN.1 — Vulnerability analysis | SECURITY.md, dependency audits |

### Target EAL

| EoS Module | Target EAL | Rationale |
|------------|:----------:|-----------|
| `eos` kernel | EAL4+ | Methodically designed, tested, reviewed |
| `eboot` bootloader | EAL4+ | Critical security boundary |
| `eipc` IPC | EAL3 | Methodically tested and checked |
| `eos-sdk` | EAL2 | Structurally tested |

---

## 4. ISO/IEC 27001

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Full Title** | Information Security Management Systems — Requirements |
| **Structure** | Clauses 4–10 (ISMS requirements) + Annex A (114 controls) |
| **Certification** | Third-party audit by accredited body |

### Annex A Controls Mapping

| Control | Title | EoS Implementation |
|---------|-------|--------------------|
| A.5.1 | Information security policies | `SECURITY.md` in all repos, compliance docs |
| A.6.1 | Internal organization | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` |
| A.8.1 | Asset management | SBOM generation, dependency tracking |
| A.9.1 | Access control policy | `eos` ACL, `eipc` capability system |
| A.9.2 | User access management | `eipc` authentication, session management |
| A.9.4 | System and application access control | `eboot` secure boot, `eos` keystore |
| A.10.1 | Cryptographic controls | `eos` crypto services (AES, RSA, ECC, SHA) |
| A.12.1 | Operational procedures | CI/CD pipelines, documented build processes |
| A.12.2 | Protection from malware | Dependency scanning, code review |
| A.12.4 | Logging and monitoring | `eos` audit service, `eipc` audit logger |
| A.12.6 | Technical vulnerability management | `SECURITY.md` disclosure process, weekly scans |
| A.14.1 | Security requirements | Product profiles with security requirements |
| A.14.2 | Security in development processes | CI gates, PR reviews, automated testing |
| A.16.1 | Management of security incidents | Vulnerability response process (48-hour SLA) |
| A.18.1 | Compliance with legal requirements | MIT license, SPDX compliance, SBOM |

### ISMS Process Mapping

| ISO 27001 Clause | EoS Process |
|------------------|-------------|
| 4 — Context | EoS ecosystem scope defined in `.github` org profile |
| 5 — Leadership | Maintainer roles in `CONTRIBUTING.md` |
| 6 — Planning | Product profiles, compliance documentation |
| 7 — Support | Documentation, architecture guides, getting-started |
| 8 — Operation | CI/CD pipelines, build system, release process |
| 9 — Performance evaluation | Test coverage, CI metrics, nightly/weekly runs |
| 10 — Improvement | CHANGELOG tracking, issue management, PR workflow |

---

## 5. EoS Security Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Applications                        │
├─────────────────────────────────────────────────────┤
│  eipc Security Layer                                 │
│  ┌──────────┬────────────┬──────────┬─────────────┐ │
│  │   Auth   │ Capability │   HMAC   │   Replay    │ │
│  │ (session)│  (authz)   │(integrity)│ (freshness) │ │
│  └──────────┴────────────┴──────────┴─────────────┘ │
│  ┌──────────────────────────────────────────────────┐│
│  │              Keyring (key lifecycle)              ││
│  └──────────────────────────────────────────────────┘│
├─────────────────────────────────────────────────────┤
│  eos Security Services                               │
│  ┌──────────┬────────────┬──────────┬─────────────┐ │
│  │  Crypto  │  Keystore  │   ACL    │    Audit    │ │
│  │(AES,RSA) │ (key store)│ (access) │  (logging)  │ │
│  └──────────┴────────────┴──────────┴─────────────┘ │
├─────────────────────────────────────────────────────┤
│  eboot Verified Boot                                 │
│  ┌──────────┬────────────┬──────────────────────────┐│
│  │  Stage 1 │  Stage 2   │  Firmware Signature      ││
│  │ (ROM)    │ (verified) │  Validation              ││
│  └──────────┴────────────┴──────────────────────────┘│
├─────────────────────────────────────────────────────┤
│  Hardware Root of Trust                              │
└─────────────────────────────────────────────────────┘
```

---

## 6. Certification Roadmap

| Phase | Target | Timeline | Status |
|-------|--------|----------|--------|
| 1 | Document security architecture | v0.1.0 | ✅ Complete |
| 2 | Implement FIPS 140-3 Level 1 self-tests | v0.2.0 | 📋 Planned |
| 3 | Common Criteria EAL2 evaluation prep | v0.3.0 | 📋 Planned |
| 4 | ISO/IEC 27001 ISMS documentation | v0.2.0 | 📋 Planned |
| 5 | FIPS 140-3 Level 1 validation | v1.0.0 | 📋 Planned |
| 6 | Common Criteria EAL4+ evaluation | v1.0.0 | 📋 Planned |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial security certifications document |
