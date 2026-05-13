<div align="center">

<img src="https://raw.githubusercontent.com/embeddedos-org/eos/master/docs/book/cover.png" width="180" alt="EmbeddedOS">

# 🚀 EmbeddedOS

### *The Operating System for Every Device — from microcontrollers to spacecraft.*

A modular, multi-platform embedded OS with on-device AI inference, secure IPC,
A/B-slot bootloader, browser engine, multi-model database, office suite, mobile
apps, simulation, and full developer tooling. **Production today:** ARM Cortex-M
kernel + Linux host backend + STM32F407 BSP. More backends and architectures on
the roadmap.

<br>

[![Website](https://img.shields.io/badge/🌐_Website-embeddedos--org.github.io-58a6ff?style=for-the-badge)](https://embeddedos-org.github.io)
[![Books](https://img.shields.io/badge/📚_Books-14_titles-3fb950?style=for-the-badge)](https://embeddedos-org.github.io/books.html)
[![Stacks](https://img.shields.io/badge/🏭_Stacks-eFab-e3b341?style=for-the-badge)](https://embeddedos-org.github.io/stacks/)
[![App Store](https://img.shields.io/badge/🏪_App_Store-Browse-f0883e?style=for-the-badge)](https://embeddedos-org.github.io/eApps/)

[![Docs](https://img.shields.io/badge/📖_Docs-13_modules-79c0ff?style=flat-square)](https://embeddedos-org.github.io/docs/)
[![Get Started](https://img.shields.io/badge/🛠_Get_Started-Quickstart-f778ba?style=flat-square)](https://embeddedos-org.github.io/getting-started.html)
[![Hardware Lab](https://img.shields.io/badge/🔬_Hardware_Lab-Boards-bc8cff?style=flat-square)](https://embeddedos-org.github.io/hardware-lab.html)
[![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)](https://opensource.org/licenses/MIT)

<br>

**13 Products** · **14 Books** · **60+ Apps** · **41 Product Profiles** · **52+ Platforms** · **300+ APIs**

</div>

---

## 🧭 What we ship

EmbeddedOS is **13 small, independently-versioned product repositories** that
compose into one coherent stack. Each product is independently useful and
independently released; bundled deployments are managed via [eFab](https://github.com/embeddedos-org/eFab).

### 🔵 Core Platform
| | Repo | One-liner |
|---|---|---|
| ⚙️ | [**eos**](https://github.com/embeddedos-org/eos) | RTOS kernel, HAL (33 interfaces), multicore SMP/AMP, services, GDB stub, loadable drivers. |
| 🔐 | [**eBoot**](https://github.com/embeddedos-org/eBoot) | A/B embedded bootloader with RFC 8032 Ed25519, staged boot, recovery. STM32F4 production reference. |
| 📡 | [**eIPC**](https://github.com/embeddedos-org/eIPC) | Secure IPC framework — Go + C SDKs, HMAC-SHA256, replay protection, TCP / Unix / SHM transports. |
| 🛠 | [**ebuild**](https://github.com/embeddedos-org/ebuild) | Unified build system — SDK generator (14 targets), hardware analyzer, 18 CLI commands. |

### 🟣 AI &amp; Neural
| | Repo | One-liner |
|---|---|---|
| 🧠 | [**eAI**](https://github.com/embeddedos-org/eAI) | On-device AI / LLM inference — 12 curated models, agent loop, LoRA fine-tuning, federated learning. |
| 🧬 | [**eNI**](https://github.com/embeddedos-org/eNI) | Neural-interface adapter — Neuralink (1024 ch / 30 kHz), EEG, DSP, intent decoder, safety interlocks. |

### 🟢 Apps &amp; Services
| | Repo | One-liner |
|---|---|---|
| 📱 | [**eApps**](https://github.com/embeddedos-org/eApps) | Unified app store — 60+ apps across desktop, mobile, web, browser-extensions, CLI, enterprise. |
| 🗄 | [**eDB**](https://github.com/embeddedos-org/eDB) | Multi-model database — SQL + Document + Key-Value, REST API, AES-256, eBot AI queries. |
| 🌐 | [**eBrowser**](https://github.com/embeddedos-org/eBrowser) | Embedded web browser engine — HTML5 / CSS, modular rendering / network / input layers. |
| 📄 | [**eOffice**](https://github.com/embeddedos-org/eOffice) | Office suite — eDocs, eSheets, eSlides, eMail, eDrive, ePlanner, eNotes, eConnect, eForms, eSway. |

### 🟠 Tools &amp; Hardware
| | Repo | One-liner |
|---|---|---|
| 🔬 | [**EoSim**](https://github.com/embeddedos-org/EoSim) | Multi-architecture simulator — 52+ platforms, 12 architectures, native + QEMU + Renode + HIL. |
| 🎨 | [**EoStudio**](https://github.com/embeddedos-org/EoStudio) | Visual design IDE — 12 editors (3D, CAD, UI, game, hardware), 30+ code generators, LLM-assisted. |
| 🔩 | [**eCAD-Hardware-Products**](https://github.com/embeddedos-org/eCAD-Hardware-Products) | Hardware designs — KiCad PCBs, EE docs, board datasheets for reference products. |

### 🧰 Meta-repos *(not part of canon)*
| | Repo | Role |
|---|---|---|
| 🌐 | [**embeddedos-org.github.io**](https://github.com/embeddedos-org/embeddedos-org.github.io) | Source for [embeddedos-org.github.io](https://embeddedos-org.github.io) — docs, books, stacks, downloads. |
| 🏭 | [**eFab**](https://github.com/embeddedos-org/eFab) | Stack fabricator — manifest-only meta-repo. v0.1.0 ships `eai-edge` (ENI + EIPC + eAI). |
| ⚙️ | [**.github**](https://github.com/embeddedos-org/.github) | Org-wide configuration: this profile, the default `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, issue/PR templates, canon validator. |

---

## ⚡ 60-second start

```bash
# Pick your path — one of the three is enough to see something running

# 1) Simulate (no hardware needed)
pip install eosim && eosim run stm32f4 --timeout 30

# 2) Build the kernel for one of 41 product profiles
git clone https://github.com/embeddedos-org/eos.git && cd eos
cmake -B build -DEOS_PRODUCT=robot && cmake --build build

# 3) Build a curated stack via eFab
git clone https://github.com/embeddedos-org/eFab.git
cd eFab/superproject/eai-edge && cmake -B build && cmake --build build
```

Full guide: [embeddedos-org.github.io/getting-started.html](https://embeddedos-org.github.io/getting-started.html)

---

## 🧑‍💻 Contribute

Code contributions belong in the relevant downstream product repo (each ships
its own `CONTRIBUTING.md`). Org-wide policy — the default `CONTRIBUTING.md`,
`SECURITY.md`, `CODE_OF_CONDUCT.md`, and the issue/PR templates — lives in
[`embeddedos-org/.github`](https://github.com/embeddedos-org/.github). For
curated-stack profiles, manifests, and integration smoke tests: open against
[`embeddedos-org/eFab`](https://github.com/embeddedos-org/eFab).

Standards we follow: **MIT** · **Conventional Commits** · **Contributor Covenant 2.1** · **WCAG 2.1** · **SBOM (SPDX, CycloneDX)** · ISO/IEC 27001 · IEC 61508 · ISO 26262 · DO-178C · FIPS 140-3.

---

<div align="center">

[🌐 Website](https://embeddedos-org.github.io) · [📚 Books](https://embeddedos-org.github.io/books.html) · [🏭 Stacks](https://embeddedos-org.github.io/stacks/) · [🏪 Apps](https://embeddedos-org.github.io/eApps/) · [⭐ Star EoS](https://github.com/embeddedos-org/eos)

**MIT License** · Made with ❤️ by [Srikanth Patchava](https://github.com/embeddedos-org) &amp; Contributors

</div>
