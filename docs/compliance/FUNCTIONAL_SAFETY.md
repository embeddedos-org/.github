# EoS Functional Safety Compliance

> **Document**: FUNCTIONAL_SAFETY.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document covers functional safety standards applicable to EoS deployments in safety-critical domains including automotive, aerospace, medical, railway, and industrial systems.

---

## Table of Contents

1. [Overview](#1-overview)
2. [IEC 61508 — Functional Safety](#2-iec-61508--functional-safety)
3. [ISO 26262 — Automotive](#3-iso-26262--automotive)
4. [DO-178C — Aerospace](#4-do-178c--aerospace)
5. [EN 50128 — Railway](#5-en-50128--railway)
6. [EoS Product Profile Mapping](#6-eos-product-profile-mapping)
7. [EoS Safety Features](#7-eos-safety-features)
8. [Safety Lifecycle Activities](#8-safety-lifecycle-activities)
9. [Compliance Matrix](#9-compliance-matrix)

---

## 1. Overview

EoS is designed for deployment in safety-critical embedded systems. This document maps functional safety standards to EoS capabilities, product profiles, and development practices. EoS provides configurable safety features that can be enabled per product profile to meet the requirements of each domain-specific standard.

---

## 2. IEC 61508 — Functional Safety

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | IEC 61508:2010 |
| **Full Name** | Functional safety of electrical/electronic/programmable electronic safety-related systems |
| **Parts** | 7 parts covering management, hardware, software, definitions, examples, guidelines, techniques |
| **Scope** | Generic functional safety standard — basis for domain-specific standards |

### Safety Integrity Levels (SIL)

| SIL | Failure Rate (per hour) | Risk Reduction | EoS Support |
|:---:|:-----------------------:|:--------------:|:-----------:|
| **SIL 1** | 10⁻⁵ to 10⁻⁶ | Low | ✅ Supported |
| **SIL 2** | 10⁻⁶ to 10⁻⁷ | Medium | ✅ Supported |
| **SIL 3** | 10⁻⁷ to 10⁻⁸ | High | 🔶 Partial |
| **SIL 4** | 10⁻⁸ to 10⁻⁹ | Very High | 📋 Planned |

### IEC 61508 Software Requirements and EoS Alignment

| IEC 61508 Requirement | SIL 1 | SIL 2 | SIL 3 | SIL 4 | EoS Implementation |
|------------------------|:-----:|:-----:|:-----:|:-----:|---------------------|
| Structured programming | R | R | HR | HR | ✅ Enforced coding standards |
| Modular design | R | R | HR | HR | ✅ HAL/service/app layering |
| Static analysis | R | R | HR | HR | ✅ CI static analysis (cppcheck, clang-tidy) |
| Unit testing | R | R | HR | HR | ✅ Automated unit tests |
| Integration testing | R | HR | HR | HR | ✅ QEMU/eosim integration tests |
| Formal verification | — | R | R | HR | 📋 Planned |
| Fault injection testing | — | R | HR | HR | 🔶 eosim fault injection |
| Configuration management | R | R | HR | HR | ✅ Git + semantic versioning |

**Legend**: HR = Highly Recommended | R = Recommended | — = Not required

---

## 3. ISO 26262 — Automotive

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | ISO 26262:2018 |
| **Full Name** | Road vehicles — Functional safety |
| **Parts** | 12 parts covering management, concept, system, hardware, software, production, support |
| **Scope** | Automotive-specific adaptation of IEC 61508 for passenger vehicles |

### Automotive Safety Integrity Levels (ASIL)

| ASIL | Severity | Exposure | Controllability | EoS Support |
|:----:|:--------:|:--------:|:---------------:|:-----------:|
| **ASIL A** | Low | Low | High | ✅ Supported |
| **ASIL B** | Medium | Medium | Medium | ✅ Supported |
| **ASIL C** | High | Medium | Low | 🔶 Partial |
| **ASIL D** | Severe | High | Low | 📋 Planned |

### ISO 26262 Part 6 (Software) — EoS Mapping

| ISO 26262 Requirement | ASIL A | ASIL B | ASIL C | ASIL D | EoS Implementation |
|------------------------|:------:|:------:|:------:|:------:|---------------------|
| Software architecture design | ++ | ++ | ++ | ++ | ✅ Layered architecture with isolation |
| Software unit design | + | ++ | ++ | ++ | ✅ Modular component design |
| Software unit testing | + | ++ | ++ | ++ | ✅ Unit tests with coverage tracking |
| Software integration testing | + | + | ++ | ++ | ✅ eosim product simulation |
| Requirements traceability | + | ++ | ++ | ++ | ✅ Build manifest traceability |
| Static code analysis | ++ | ++ | ++ | ++ | ✅ CI pipeline enforcement |
| Memory partitioning | o | + | ++ | ++ | ✅ MPU isolation support |
| Safe state handling | + | ++ | ++ | ++ | ✅ Watchdog + safe-state transitions |

**Legend**: ++ = Highly Recommended | + = Recommended | o = No recommendation

### EoS Automotive Product Profiles

| Profile | Target | ASIL | Repo |
|---------|--------|:----:|------|
| `vehicle.py` | Infotainment, ADAS ECUs | A–B | `eosim` |
| `eos-platform/automotive` | Vehicle platform config | A–B | `eos-platform` |
| `products/vehicle_*.h` | Product header configs | A–B | `eos` |

---

## 4. DO-178C — Aerospace

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | RTCA DO-178C / EUROCAE ED-12C |
| **Full Name** | Software Considerations in Airborne Systems and Equipment Certification |
| **Supplements** | DO-330 (Tool Qualification), DO-331 (Model-Based), DO-332 (OO), DO-333 (Formal Methods) |
| **Scope** | Certification guidance for airborne software |

### Design Assurance Levels (DAL)

| DAL | Failure Condition | Example | EoS Support |
|:---:|:-----------------:|---------|:-----------:|
| **DAL A** | Catastrophic | Flight control | 📋 Planned |
| **DAL B** | Hazardous | Engine display | 📋 Planned |
| **DAL C** | Major | Navigation | 🔶 Partial |
| **DAL D** | Minor | Cabin lighting | ✅ Supported |
| **DAL E** | No effect | Entertainment | ✅ Supported |

### DO-178C Objectives — EoS Mapping

| DO-178C Objective | DAL A | DAL B | DAL C | DAL D | DAL E | EoS Implementation |
|-------------------|:-----:|:-----:|:-----:|:-----:|:-----:|---------------------|
| Requirements-based testing | ✓ | ✓ | ✓ | ✓ | — | ✅ Test cases mapped to requirements |
| Structural coverage (statement) | ✓ | ✓ | ✓ | ✓ | — | ✅ gcov/lcov in CI |
| Structural coverage (decision) | ✓ | ✓ | ✓ | — | — | 🔶 Partial coverage tooling |
| Structural coverage (MC/DC) | ✓ | ✓ | — | — | — | 📋 Planned |
| Configuration management | ✓ | ✓ | ✓ | ✓ | ✓ | ✅ Git + semantic versioning |
| Traceability | ✓ | ✓ | ✓ | ✓ | — | ✅ Build manifests |
| Tool qualification (DO-330) | ✓ | ✓ | ✓ | — | — | 📋 Planned for ebuild-tool |
| Deterministic execution | ✓ | ✓ | ✓ | — | — | ✅ Priority-based scheduler |

### EoS Aerospace Product Profiles

| Profile | Target | DAL | Repo |
|---------|--------|:---:|------|
| `aircraft.py` | Avionics display, cabin systems | D–E | `eosim` |
| `products/aircraft_*.h` | Product header configs | D–E | `eos` |

---

## 5. EN 50128 — Railway

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | EN 50128:2011 |
| **Full Name** | Railway applications — Communication, signalling and processing systems — Software for railway control and protection systems |
| **Related** | EN 50126 (RAMS), EN 50129 (Safety-related electronic systems) |
| **Scope** | Software development for railway signalling and control |

### EN 50128 SIL Levels

| SIL | Application Example | EoS Support |
|:---:|---------------------|:-----------:|
| **SIL 0** | Non-safety functions (passenger info) | ✅ Supported |
| **SIL 1** | Minor safety functions | ✅ Supported |
| **SIL 2** | Moderate safety functions | 🔶 Partial |
| **SIL 3** | Signalling interlocking | 📋 Planned |
| **SIL 4** | Train protection systems (ATP) | 📋 Planned |

### EN 50128 Techniques — EoS Mapping

| Technique | SIL 0 | SIL 1–2 | SIL 3–4 | EoS Implementation |
|-----------|:-----:|:-------:|:-------:|---------------------|
| Modular approach | R | HR | M | ✅ Component-based architecture |
| Defensive programming | R | HR | M | ✅ Input validation, bounds checking |
| Static analysis | R | HR | M | ✅ CI static analysis tools |
| Traceability | R | HR | M | ✅ Build manifest traceability |
| Formal proof | — | R | HR | 📋 Planned |
| Diverse programming | — | R | HR | 📋 Planned |

**Legend**: M = Mandatory | HR = Highly Recommended | R = Recommended

---

## 6. EoS Product Profile Mapping

### Domain-to-Standard Mapping

| Domain | Primary Standard | EoS Product Profiles | Target Level |
|--------|-----------------|----------------------|:------------:|
| **Automotive** | ISO 26262 | `vehicle.py`, automotive platform | ASIL A–B |
| **Aerospace** | DO-178C | `aircraft.py`, avionics platform | DAL D–E |
| **Medical** | IEC 61508 / IEC 62304 | `medical.py`, medical platform | SIL 1–2 |
| **Railway** | EN 50128 | `industrial.py`, railway platform | SIL 0–1 |
| **Industrial** | IEC 61508 | `industrial.py`, factory platform | SIL 1–2 |
| **Consumer** | N/A (quality only) | `iot.py`, `wearable.py`, `speaker.py` | N/A |

### Safety Feature Configuration per Profile

| Feature | Automotive | Aerospace | Medical | Railway | Industrial | Consumer |
|---------|:----------:|:---------:|:-------:|:-------:|:----------:|:--------:|
| Watchdog timer | ✅ | ✅ | ✅ | ✅ | ✅ | Optional |
| MPU isolation | ✅ | ✅ | ✅ | ✅ | ✅ | Optional |
| Redundant execution | ✅ | ✅ | ✅ | ✅ | Optional | — |
| Audit logging | ✅ | ✅ | ✅ | ✅ | ✅ | Optional |
| Secure boot | ✅ | ✅ | ✅ | ✅ | ✅ | Optional |
| Safe-state transition | ✅ | ✅ | ✅ | ✅ | Optional | — |
| Stack overflow detection | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## 7. EoS Safety Features

### Watchdog Timer

- **Implementation**: Hardware and software watchdog support via HAL
- **Configuration**: Timeout period, recovery action (reset, safe-state, log)
- **Repo**: `eos` (kernel), `eos-platform` (product configs)

### Redundancy

- **Dual execution**: Critical tasks run on redundant paths with result comparison
- **Voting logic**: 2-of-3 voting for highest-integrity decisions
- **Repo**: `eos` (scheduler), `eos-platform` (redundancy config)

### Audit Logging

- **Tamper-evident**: HMAC-signed log entries via `eipc` security module
- **Persistent**: Logs survive reboot via dedicated flash partition
- **Repo**: `eos` (logging service), `eipc` (HMAC signing)

### MPU Isolation

- **Memory Protection Unit**: Hardware-enforced process isolation
- **Privilege levels**: Kernel (privileged) / User (unprivileged) separation
- **Stack guard**: Dedicated guard regions between task stacks
- **Repo**: `eos` (kernel MPU driver)

### Secure Boot

- **Chain of trust**: `eboot` → kernel → services → applications
- **Signature verification**: RSA/ECC signature on each stage
- **Rollback protection**: Monotonic counter prevents downgrade attacks
- **Repo**: `eboot` (bootloader), `eos` (kernel verification)

### Safe-State Transition

- **Fault detection**: Watchdog expiry, MPU violation, stack overflow, assertion failure
- **Recovery actions**: Configurable per product — restart task, restart system, enter safe mode
- **Safe mode**: Minimal kernel with diagnostic output, no application execution
- **Repo**: `eos` (fault handler), `eos-platform` (safe-state config)

---

## 8. Safety Lifecycle Activities

### Development Phase

| Activity | Tool/Process | Standard Requirement |
|----------|-------------|----------------------|
| Hazard analysis | Risk register (`risk_register.md`) | IEC 61508, ISO 26262, DO-178C |
| Safety requirements | Product profile configs | All standards |
| Architecture design | `CODE_STRUCTURE.md`, docs | All standards |
| Coding standards | `.clang-format`, `.clang-tidy` | IEC 61508, ISO 26262 |
| Static analysis | CI pipeline (cppcheck, clang-tidy) | All standards |
| Unit testing | CI pipeline (CTest, pytest) | All standards |
| Integration testing | eosim product simulation | All standards |
| Coverage analysis | gcov/lcov in CI | DO-178C, ISO 26262 |
| Configuration management | Git + semantic versioning | All standards |

### Verification Phase

| Activity | Tool/Process | Coverage |
|----------|-------------|----------|
| Requirements traceability | Build manifests → test cases | Full |
| Structural coverage | gcov/lcov statement coverage | Statement level |
| Fault injection | eosim fault injection framework | Selected scenarios |
| Hardware-in-the-loop | eosim HIL session + serial bridge | Selected platforms |
| Regression testing | CI nightly/weekly workflows | Full test suite |

---

## 9. Compliance Matrix

| Standard | Requirement | EoS Status |
|----------|-------------|------------|
| IEC 61508 SIL 1 | Software systematic capability | ✅ Supported |
| IEC 61508 SIL 2 | Enhanced testing and analysis | ✅ Supported |
| IEC 61508 SIL 3 | Formal methods, fault injection | 🔶 Partial |
| IEC 61508 SIL 4 | Full formal verification | 📋 Planned |
| ISO 26262 ASIL A | Basic safety requirements | ✅ Supported |
| ISO 26262 ASIL B | Enhanced testing, static analysis | ✅ Supported |
| ISO 26262 ASIL C | Memory partitioning, MC/DC | 🔶 Partial |
| ISO 26262 ASIL D | Full MC/DC, diverse design | 📋 Planned |
| DO-178C DAL E | No safety objectives | ✅ Supported |
| DO-178C DAL D | Basic testing and traceability | ✅ Supported |
| DO-178C DAL C | Decision coverage | 🔶 Partial |
| DO-178C DAL B | MC/DC coverage | 📋 Planned |
| DO-178C DAL A | Full MC/DC + tool qualification | 📋 Planned |
| EN 50128 SIL 0 | Non-safety functions | ✅ Supported |
| EN 50128 SIL 1 | Basic safety techniques | ✅ Supported |
| EN 50128 SIL 2 | Enhanced defensive programming | 🔶 Partial |
| EN 50128 SIL 3–4 | Formal proof, diverse programming | 📋 Planned |
| Watchdog timer | Hardware/software watchdog | ✅ Implemented |
| MPU isolation | Hardware memory protection | ✅ Implemented |
| Secure boot chain | eboot → kernel → apps | ✅ Implemented |
| Audit logging | HMAC-signed persistent logs | ✅ Implemented |
| Safe-state transitions | Configurable fault recovery | ✅ Implemented |
| Redundant execution | Dual-path with voting | 🔶 Partial |

**Legend**: ✅ Supported/Implemented | 🔶 Partial | 📋 Planned

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial functional safety compliance document |
# EoS Functional Safety Compliance

> **Document**: FUNCTIONAL_SAFETY.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document maps EoS safety-critical features to international functional safety standards.

---

## Table of Contents

1. [Overview](#1-overview)
2. [IEC 61508 — Functional Safety of E/E/PE Systems](#2-iec-61508)
3. [ISO 26262 — Road Vehicles](#3-iso-26262)
4. [DO-178C — Airborne Systems](#4-do-178c)
5. [EN 50128 — Railway Software](#5-en-50128)
6. [EoS Safety Architecture](#6-eos-safety-architecture)
7. [Safety Compliance Matrix](#7-safety-compliance-matrix)

---

## 1. Overview

EoS provides a foundation for safety-critical embedded systems. While EoS itself is not pre-certified, its architecture and verification infrastructure are aligned with IEC 61508, ISO 26262, DO-178C, and EN 50128 to facilitate downstream certification.

### Safety-Critical EoS Components

| Component | Repo | Safety Role |
|-----------|------|-------------|
| **eboot Safety Bootloader** | `eboot` | Verified boot chain, firmware integrity, cryptographic signature validation |
| **eos Watchdog Service** | `eos` | System liveness monitoring, automatic recovery, timeout enforcement |
| **eos Crypto Verification** | `eos` | SHA-256/512, AES, RSA, ECC, CRC for data integrity |
| **eos Secure Storage** | `eos` | Tamper-resistant key storage, ACL enforcement |
| **eos Audit Service** | `eos` | Immutable audit trail for safety-relevant events |
| **eipc Policy Engine** | `eipc` | Action classification (safe/controlled/restricted), capability enforcement |
| **eipc Integrity** | `eipc` | HMAC-SHA256 message integrity, replay protection |
| **eosim Simulator** | `eosim` | Pre-deployment validation, HIL-ready simulation |

---

## 2. IEC 61508

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Full Title** | Functional Safety of Electrical/Electronic/Programmable Electronic Safety-Related Systems |
| **Scope** | All industries using E/E/PE safety functions |
| **Safety Integrity Levels** | SIL 1 (lowest) through SIL 4 (highest) |

### EoS Alignment to IEC 61508 Part 3 (Software)

| Requirement | SIL | EoS Implementation |
|-------------|-----|---------------------|
| Software safety requirements | 1–4 | Product profiles in `eos/products/*.h` define safety requirements per product |
| Software architecture design | 1–4 | Modular HAL architecture with defined interfaces |
| Module testing | 1–4 | Unit tests per module, coverage reporting in CI |
| Integration testing | 2–4 | QEMU integration tests across x86_64, aarch64, riscv64 |
| HW/SW integration testing | 2–4 | `eosim` HIL simulation with hardware models |
| Safety validation | 1–4 | `eosim` product-specific validation, safety monitor checks |
| Configuration management | 1–4 | Git + SemVer + CI/CD + SHA256 checksums |
| Defensive programming | 2–4 | Watchdog timers, CRC checks, bounds checking |
| Diversity and redundancy | 3–4 | Multicore SMP/AMP support, redundant communication |
| Failure detection | 1–4 | Watchdog, health monitoring, audit logging |

### Techniques and Measures (Table A)

| Technique | Recommendation | EoS Status |
|-----------|---------------|------------|
| Structured programming | HR (all SILs) | ✅ Enforced via coding standards |
| Defensive programming | R/HR | ✅ Watchdog, CRC, bounds checks |
| Modular approach | HR (all SILs) | ✅ HAL abstraction layers |
| Static analysis | R/HR | ✅ Compiler warnings, lint |
| Dynamic testing | HR (all SILs) | ✅ QEMU + eosim |
| Test coverage (statement) | R/HR | ✅ CI coverage reporting |
| Test coverage (branch) | R/HR | 🔄 In progress |
| Formal verification | R (SIL 3–4) | 📋 Planned |

---

## 3. ISO 26262

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Full Title** | Road Vehicles — Functional Safety |
| **Scope** | Automotive E/E systems |
| **Safety Levels** | ASIL A (lowest) through ASIL D (highest), plus QM |

### Automotive HAL Mapping

| Domain | EoS HAL Interface | Repo |
|--------|--------------------|------|
| Powertrain | `eos_motor_*`, `eos_can_*` | `eos` |
| Chassis | `eos_imu_*`, `eos_motor_*` | `eos` |
| Body electronics | `eos_gpio_*`, `eos_pwm_*`, `eos_display_*` | `eos` |
| ADAS | `eos_radar_*`, `eos_camera_*`, `eos_gnss_*`, `eos_imu_*` | `eos` |
| Infotainment | `eos_display_*`, `eos_audio_*`, `eos_hdmi_*`, `eos_bluetooth_*` | `eos` |
| V2X Communication | `eos_can_*`, `eos_ethernet_*`, `eos_cellular_*` | `eos` |
| Secure Gateway | `eos_crypto_*`, `eos_acl_*`, `eos_secure_boot_*` | `eos`, `eboot` |

### ASIL Decomposition for EoS Modules

| Module | Recommended ASIL | Rationale |
|--------|-----------------|-----------|
| `eboot` | ASIL D | Boot chain integrity is safety-critical |
| `eos/kernel` | ASIL C–D | Task scheduling, memory management |
| `eos/hal` | ASIL B–D | Hardware interface reliability |
| `eos/crypto` | ASIL C | Data integrity for safety signals |
| `eos/watchdog` | ASIL D | System liveness monitoring |
| `eipc` | ASIL B | Inter-process communication reliability |
| `eai` | QM–ASIL A | AI inference (advisory, not control) |

---

## 4. DO-178C

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Full Title** | Software Considerations in Airborne Systems and Equipment Certification |
| **Scope** | Avionics software |
| **Assurance Levels** | DAL A (catastrophic) through DAL E (no effect) |
| **Supplements** | DO-330 (tool qualification), DO-331 (model-based), DO-332 (OO), DO-333 (formal methods) |

### EoS Alignment to DO-178C Objectives

| Objective | DAL | EoS Implementation |
|-----------|-----|---------------------|
| Planning process | A–E | CI/CD workflows, documented build chains |
| Software requirements | A–D | Aerospace product profiles: `flight_controller.h`, `avionics_display.h` |
| Software design | A–D | Modular architecture, documented interfaces |
| Coding standards | A–C | C99, static analysis, coding guidelines |
| Low-level testing | A–B | Unit tests with coverage |
| Integration testing | A–C | QEMU boot tests, `eosim` aircraft simulation |
| Structural coverage (statement) | A–C | CI coverage reporting |
| Structural coverage (MC/DC) | A | 📋 Planned for DAL A certification |
| Configuration management | A–E | Git + SemVer + SHA256 |
| Tool qualification (DO-330) | A–D | `ebuild`, `ebuild-tool` tool qualification artifacts |

### DAL Mapping for EoS Modules

| Module | Recommended DAL | Usage Context |
|--------|----------------|---------------|
| `eboot` | DAL B | Boot integrity for avionics |
| `eos/kernel` | DAL B | Deterministic scheduling |
| `eos/watchdog` | DAL A | Safety monitoring |
| `eos/crypto` | DAL C | Data authentication |
| `eipc` | DAL C | Avionics data bus communication |

---

## 5. EN 50128

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Full Title** | Railway Applications — Software for Railway Control and Protection Systems |
| **Scope** | Software for railway signalling and control |
| **Safety Levels** | SIL 0 (non-safety) through SIL 4 (highest) |
| **Related** | EN 50126 (RAMS), EN 50129 (electronic systems) |

### EoS Alignment

| Requirement | EoS Implementation |
|-------------|---------------------|
| Software requirements | Product profiles for railway signalling applications |
| Architecture | Modular HAL with CAN/Ethernet for train communication |
| Coding standards | C99, no dynamic allocation in safety paths |
| Testing | Unit + QEMU + eosim simulation |
| Safety monitoring | Watchdog, integrity checks, audit logging |
| Configuration management | Git + SemVer + SHA256 checksums |
| Fault tolerance | Multicore redundancy, communication integrity (HMAC) |

---

## 6. EoS Safety Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Application Layer                   │
│  (Product-specific safety functions)                 │
├─────────────────────────────────────────────────────┤
│              Safety Services Layer                   │
│  Watchdog │ Audit │ Crypto │ Secure Storage │ ACL   │
├─────────────────────────────────────────────────────┤
│           Communication Layer (eipc)                 │
│  Auth │ Capability │ HMAC │ Replay Protection       │
├─────────────────────────────────────────────────────┤
│              Kernel & HAL Layer (eos)                │
│  Task Mgmt │ Mutex │ Timer │ 33 HAL Interfaces      │
├─────────────────────────────────────────────────────┤
│            Boot Layer (eboot)                        │
│  Verified Boot │ Firmware Integrity │ Crypto Sigs    │
├─────────────────────────────────────────────────────┤
│              Hardware                                │
└─────────────────────────────────────────────────────┘
```

### Safety Mechanisms

| Mechanism | Layer | Description |
|-----------|-------|-------------|
| Verified Boot | eboot | Cryptographic signature check before kernel execution |
| Watchdog Timer | eos | Hardware/software watchdog with configurable timeout |
| CRC Integrity | eos | CRC-32 on critical data structures |
| HMAC Verification | eipc | SHA-256 HMAC on all inter-process messages |
| Replay Protection | eipc | Sliding-window sequence number validation |
| Capability Auth | eipc | Fine-grained action authorization |
| Audit Trail | eos | Immutable log of safety-relevant events |
| Secure Storage | eos | Encrypted storage for keys and safety parameters |

---

## 7. Safety Compliance Matrix

| Standard | Domain | SIL/ASIL/DAL | EoS Repos | Status |
|----------|--------|:------------:|-----------|--------|
| IEC 61508 | General | SIL 1–3 | eos, eboot, eosim | ✅ Architecture aligned |
| ISO 26262 | Automotive | QM–ASIL D | eos, eboot, eipc, eosim | ✅ Architecture aligned |
| DO-178C | Aerospace | DAL E–B | eos, eboot, eosim | ✅ Architecture aligned |
| EN 50128 | Railway | SIL 0–3 | eos, eboot, eipc, eosim | ✅ Architecture aligned |

> **Note**: "Architecture aligned" means EoS design patterns and processes support certification but formal certification must be pursued per deployment.

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial functional safety document |
