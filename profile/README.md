<div align="center">

# EmbeddedOS

**The Complete Embedded Operating System**

A unified ecosystem of OS kernel, bootloader, AI runtime, IPC, neural interface, build system, simulator, applications, developer tools, browser, database, office suite, and mobile services — targeting 14+ hardware platforms across 12 architectures.

**41 product profiles** | **33 HAL peripherals** | **300+ unit tests** | **12 architectures** | **24 board ports** | **60+ apps**

[![Version](https://img.shields.io/badge/version-0.1.0-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![CI](https://img.shields.io/badge/CI-passing-brightgreen)]()

[Website](https://www.embeddedos.org) | [Developer Portal](https://embeddedos-org.github.io) | [App Store](https://embeddedos-org.github.io/eApps/) | [Quick Start](#quick-start) | [Releases](#releases)

</div>

---

## Architecture

```
+------------------------------------------------------------------+
|              eApps — Unified App Store & Marketplace              |
|  46 Native | 32 Mobile | 34 Web | 20 Browser Ext | 22 CLI Tools |
|  4 Desktop (eOffice, EoStudio, EoSim, eBrowser) | 16 Enterprise  |
+------------------------------------------------------------------+
        |                    |                    |
+----------------+  +----------------+  +------------------+
|   EAI + ENI    |  |      EIPC      |  |   EoS Services   |
|  LLM Inference |  |  Go + C SDK    |  |  Crypto | OTA    |
|  Agent Loop    |  |  HMAC Auth     |  |  Sensor | Motor  |
|  BCI Adapter   |  |  TCP/Unix/SHM  |  |  FS | Net        |
+----------------+  +----------------+  +------------------+
        |                    |                    |
+------------------------------------------------------------------+
|                   EoS Core + eBoot                               |
|  RTOS Kernel: tasks, sync, IPC, multicore scheduling             |
|  Bootloader: 24 boards, secure boot, A/B slots, recovery        |
|  Debug: GDB stub, core dump, ring buffer logging (6 levels)      |
|  Drivers: loadable framework, 19 device classes, device tree     |
+------------------------------------------------------------------+
        |                    |                    |
+------------------------------------------------------------------+
|                   HAL — 33 Peripherals                            |
|  GPIO | UART | SPI | I2C | CAN | WiFi | BLE | USB | ADC | PWM  |
|  Timer | DMA | GPU | Camera | IMU | Display | Audio | Ethernet  |
+------------------------------------------------------------------+
        |                    |                    |
+----------------+  +----------------+  +------------------+
|     EoSim      |  |     eBuild     |  | Physical Boards  |
|  52+ Platforms |  |  SDK Generator |  |  ARM | RISC-V    |
|  12 Arches     |  |  14 Targets    |  |  x86 | Xtensa   |
|  Native Engine |  |  Gated Release |  |  MIPS | PPC     |
+----------------+  +----------------+  +------------------+
```

## Repositories

### Core Platform

| Repo | Description | Key Features |
|------|-------------|--------------|
| [**eos**](https://github.com/embeddedos-org/eos) | Multi-platform Embedded OS | HAL (33 peripherals), RTOS kernel (tasks, sync, IPC, multicore), crypto (SHA-256, AES, RSA), OTA, filesystem, sensor fusion, PID motor control, GDB remote stub, core dump, service manager, loadable driver framework, device tree parser, logging (6 levels) |
| [**eboot**](https://github.com/embeddedos-org/eboot) | Universal Bootloader | 24 board ports across 10 architectures, A/B firmware slots, secure boot chain, crypto verification, recovery mode, UEFI-style device table, multicore SMP/AMP/lockstep boot |
| [**eipc**](https://github.com/embeddedos-org/eipc) | Secure IPC | Go server + C SDK, HMAC-SHA256 authentication, replay protection, frame protocol, TCP/Unix/shared memory transports, priority lanes P0-P3, pub/sub broker, policy engine |

### Intelligence

| Repo | Description | Key Features |
|------|-------------|--------------|
| [**eai**](https://github.com/embeddedos-org/eai) | Embedded AI Layer | Two-tier (EAI-Min 50KB + EAI-Framework), llama.cpp runtime with 12 curated LLM models (TinyLlama→Llama 3.2 8B), agent loop (think-act-observe), LoRA fine-tuning, federated learning, 8-layer security, power-aware inference |
| [**eni**](https://github.com/embeddedos-org/eni) | Embedded Neural Interface | Neuralink adapter (1024 channels, 30kHz), EEG headset provider, DSP (FIR/IIR/FFT), lightweight neural net, intent decoder, neurofeedback, stimulator with safety interlocks, EIPC bridge |

### Tools & Build

| Repo | Description | Key Features |
|------|-------------|--------------|
| [**ebuild**](https://github.com/embeddedos-org/ebuild) | Build System + SDK Generator | 18 CLI commands, Yocto-style SDK generation for 14 targets, hardware analyzer (KiCad/YAML), deliverable packager, gated release pipeline, 6 project templates |
| [**eosim**](https://github.com/embeddedos-org/eosim) | Multi-Architecture Simulator | EoSim native engine, 52+ platforms, 12 architectures, CPU + memory + peripherals, QEMU/Renode/HIL bridge, GUI dashboard, cluster simulation |

### Applications & Marketplace

| Repo | Description | Key Features |
|------|-------------|-------------------------------|
| [**eApps**](https://github.com/embeddedos-org/eApps) | **Unified App Store & Marketplace** | 60+ apps across 8 categories: 46 native C/LVGL apps, 4 desktop apps (eOffice, EoStudio, EoSim, eBrowser), 32 mobile Flutter apps, 34 web PWAs, 20 browser extensions, 14 dev tools, 22 CLI tools, 16 enterprise deployments. Automated CI/CD → [**Live App Store**](https://embeddedos-org.github.io/eApps/) |
| [**EoStudio**](https://github.com/embeddedos-org/EoStudio) | Design Suite | 12 editors (3D, CAD, image, game, UI, UML, simulation, database, hardware, IDE), 30+ code generators, LLM integration |

### Infrastructure & Web

| Repo | Description | Key Features |
|------|-------------|-------------------------------|
| [**embeddedos-org.github.io**](https://github.com/embeddedos-org/embeddedos-org.github.io) | Developer Portal | Documentation, getting started guides, hardware lab, flow diagrams, responsive design |
| [**www.embeddedos.org**](https://github.com/embeddedos-org/www.embeddedos.org) | Foundation Website | 26 pages, product pages for all 13 projects, research articles, certification programs, membership, careers, internships |

## Websites

| Site | URL | Purpose |
|------|-----|---------|
| **Foundation** | [www.embeddedos.org](https://www.embeddedos.org) | Research foundation homepage — products, certifications, membership, careers |
| **Developer Portal** | [embeddedos-org.github.io](https://embeddedos-org.github.io) | Technical docs, getting started, hardware lab, platform flow |
| **App Store** | [embeddedos-org.github.io/eApps](https://embeddedos-org.github.io/eApps/) | Browse, filter, download 60+ apps for all platforms |

## Supported Hardware

| Target | Architecture | CPU | Vendor / SoC | Class |
|--------|-------------|-----|-------------|-------|
| `stm32f4` | ARM Cortex-M4 | cortex-m4 | ST STM32F407 | MCU |
| `stm32h7` | ARM Cortex-M7 | cortex-m7 | ST STM32H743 | MCU |
| `stm32l4` | ARM Cortex-M4 | cortex-m4 | ST STM32L4 | MCU |
| `nrf52` | ARM Cortex-M4F | cortex-m4 | Nordic nRF52840 | MCU |
| `samd51` | ARM Cortex-M4F | cortex-m4 | Microchip ATSAMD51 | MCU |
| `rp2040` | ARM Cortex-M0+ | cortex-m0+ | RPi RP2040 | MCU |
| `raspi4` | AArch64 | cortex-a72 | Broadcom BCM2711 | SBC |
| `raspi3` | AArch64 | cortex-a53 | Broadcom BCM2837 | SBC |
| `imx8m` | AArch64 | cortex-a53 | NXP i.MX8M | SoC |
| `am64x` | AArch64 | cortex-a53+r5f | TI AM6442 | SoC |
| `riscv_virt` | RISC-V 64 | rv64gc | EoSim virt | Virtual |
| `sifive_u` | RISC-V 64 | u74 | SiFive FU740 | SBC |
| `esp32` | Xtensa LX6 | xtensa | Espressif ESP32 | MCU |
| `x86_64` | x86_64 | generic | Generic EFI PC | PC |

## Quick Start

```bash
# Build the embedded OS
git clone https://github.com/embeddedos-org/eos.git && cd eos
cmake -B build -DEOS_PRODUCT=robot -DEOS_BUILD_TESTS=ON
cmake --build build && ctest --test-dir build

# Build the bootloader for STM32F4
git clone https://github.com/embeddedos-org/eboot.git && cd eboot
cmake -B build -DEBLDR_BOARD=stm32f4 && cmake --build build

# Install the build system
git clone https://github.com/embeddedos-org/ebuild.git && cd ebuild
pip install -e .
ebuild build --target raspi4 --with eai,eni,eipc

# Run the simulator
pip install eosim
eosim list && eosim run stm32f4 --timeout 30

# Start IPC server
git clone https://github.com/embeddedos-org/eipc.git && cd eipc
go run ./cmd/eipc-server

# Build eApps (60+ cross-platform apps)
git clone --recursive https://github.com/embeddedos-org/eApps.git && cd eApps
cmake -B build -DEAPPS_PORT=sdl2 && cmake --build build

# Browse the App Store
# Visit https://embeddedos-org.github.io/eApps/
```

## eApps — Unified Marketplace

The [eApps](https://github.com/embeddedos-org/eApps) repository is the single source of truth for all EoS applications:

| Category | Count | Technologies | Delivery |
|---|---|---|---|
| **Native Apps** | 46 | C + LVGL | Binaries, WASM |
| **Desktop Apps** | 4 | Electron, Python, C/SDL2 | `.exe` `.dmg` `.AppImage` |
| **Mobile Apps** | 32 | Flutter (Android + iOS) | `.apk` `.aab` `.ipa` |
| **Web Apps** | 34 | HTML5/JS/WASM PWA | GitHub Pages |
| **Browser Extensions** | 20 | WebExtensions Manifest V3 | `.zip` `.crx` `.xpi` |
| **Dev Tools** | 14 | VS Code, JetBrains, Vim | `.vsix` `.jar` |
| **CLI Tools** | 22 | Node.js, Python | npm, pip |
| **Enterprise** | 16 | Docker, Helm, MSI | Images, charts |

**Headline Products:** eOffice (11-app suite), EoStudio (12-editor IDE), EoSim (52+ platform simulator), eBrowser (embedded web engine), eServiceApps (5 Flutter mobile apps)

🏪 **[Browse the App Store →](https://embeddedos-org.github.io/eApps/)**

## CI/CD

Every repository runs automated CI/CD via GitHub Actions:

| Workflow | Schedule | Coverage |
|----------|----------|----------|
| **CI** | Every push/PR | Build + test on all platforms (Linux × Windows × macOS) |
| **Nightly** | 2:00 AM UTC daily | Full regression suite across all platforms |
| **Weekly** | Monday 6:00 AM UTC | Comprehensive build + dependency audit |
| **EoSim Sanity** | 4:00 AM UTC daily | Simulation and boot validation across platform configs |
| **Simulation Test** | 3:00 AM UTC daily | QEMU/EoSim platform simulation (7+ architectures) |
| **Release** | Tag-triggered | Build + test + artifact upload to GitHub Releases |

### Cross-Repo Dispatch

Changes in core repos (eos, eboot) automatically trigger CI in dependent repos — ensuring the entire ecosystem stays validated.

## Standards Compliance

| Category | Standards |
|----------|----------|
| Systems Engineering | ISO/IEC/IEEE 15288:2023, ISO/IEC 12207, ISO/IEC/IEEE 42010 |
| Quality & Testing | ISO/IEC 25000, ISO/IEC 25010, ISO/IEC/IEEE 29119, ISO 9001 |
| Security | ISO/IEC 27001, ISO/IEC 15408, FIPS 140-3, ISO/IEC 27701 |
| Safety | IEC 61508, ISO 26262, DO-178C, EN 50128 |
| Supply Chain | NTIA SBOM, SPDX, CycloneDX, OpenChain (ISO/IEC 5230) |
| Platform | POSIX (IEEE 1003), Linux Standard Base, WCAG 2.1 |

## License

MIT — see individual repositories for details.
