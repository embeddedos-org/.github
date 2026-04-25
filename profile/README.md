<div align="center">

<img src="https://raw.githubusercontent.com/embeddedos-org/eos/master/docs/book/cover.png" width="180" alt="EoS Cover">

# 🚀 EmbeddedOS

### The Complete Open-Source Embedded Operating System

*A unified ecosystem spanning OS kernel, bootloader, AI runtime, IPC, neural interface, build system, simulator, IDE, browser, database, office suite, trading platform, and hardware designs — across 12 architectures and 83+ board ports.*

<br>

[![Version](https://img.shields.io/badge/version-1.0.0-blue?style=for-the-badge&logo=semver)](https://github.com/embeddedos-org/eos)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge&logo=opensourceinitiative)](LICENSE)
[![CI](https://img.shields.io/badge/CI%2FCD-passing-brightgreen?style=for-the-badge&logo=githubactions)](https://github.com/embeddedos-org)
[![Books](https://img.shields.io/badge/📚_books-16_guides-purple?style=for-the-badge)](https://embeddedos-org.github.io/books.html)
[![Diagrams](https://img.shields.io/badge/🖼_diagrams-65+-orange?style=for-the-badge)](https://embeddedos-org.github.io/books.html)

<br>

**83 Board Ports** · **15 Products** · **41 Product Categories** · **500K+ Lines** · **65+ Diagrams** · **180+ Citations**

<br>

[🌐 Website](https://embeddedos-org.github.io) · [📚 Book Library](https://embeddedos-org.github.io/books.html) · [🏪 App Store](https://embeddedos-org.github.io/eApps/) · [📖 Docs](https://embeddedos-org.github.io/docs/) · [🛠 Get Started](https://embeddedos-org.github.io/getting-started.html)

</div>

---

## 🏗️ Platform Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                    📱 eApps — Unified App Marketplace                │
│    46 Native │ 32 Mobile │ 34 Web │ 20 Extensions │ 22 CLI Tools    │
│    🖥 eOffice │ 🎨 EoStudio │ 🔬 EoSim │ 🌐 eBrowser │ 🤖 eVera    │
├──────────────────────────────────────────────────────────────────────┤
│  🧠 eAI + eNI        │  📡 eIPC           │  🔧 EoS Services       │
│  TinyML · LLM · BCI  │  gRPC · Pub/Sub    │  Crypto · OTA · FS     │
│  LoRA · Federated     │  HMAC · 5 Trans.   │  Sensor · Motor · UI   │
├──────────────────────────────────────────────────────────────────────┤
│                    ⚙️ EoS Kernel + 🔐 eBoot                         │
│  RTOS: Priority Preemptive │ Scheduler │ IPC │ Memory │ Multicore   │
│  Boot: 83 boards │ Secure boot │ A/B slots │ Ed25519 │ Anti-rollback│
├──────────────────────────────────────────────────────────────────────┤
│                    🔌 HAL — 33 Peripherals                           │
│  GPIO │ UART │ SPI │ I2C │ CAN │ WiFi │ BLE │ USB │ ADC │ PWM      │
│  Timer │ DMA │ GPU │ Camera │ IMU │ Display │ Audio │ Ethernet      │
├──────────────────────────────────────────────────────────────────────┤
│  🔬 EoSim           │  🛠 ebuild          │  🔩 Physical Boards     │
│  QEMU · Renode · FMI │  CMake · Meson · Yoc│  ARM · RISC-V · x86   │
│  52+ Virtual Platforms│  Ninja · Conan      │  Xtensa · MIPS · PPC  │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 📦 Repositories

### 🔵 Core Platform

| | Repo | Description | Stats |
|---|------|-------------|-------|
| ⚙️ | [**eos**](https://github.com/embeddedos-org/eos) | Real-Time Operating System | ![](https://img.shields.io/badge/HAL-33_peripherals-blue) ![](https://img.shields.io/badge/boards-83-green) |
| 🔐 | [**eBoot**](https://github.com/embeddedos-org/eBoot) | Secure Bootloader Platform | ![](https://img.shields.io/badge/crypto-Ed25519-purple) ![](https://img.shields.io/badge/A%2FB-slots-orange) |
| 📡 | [**eIPC**](https://github.com/embeddedos-org/eIPC) | Inter-Process Communication | ![](https://img.shields.io/badge/transports-5-blue) ![](https://img.shields.io/badge/auth-HMAC-red) |
| 🛠 | [**ebuild**](https://github.com/embeddedos-org/ebuild) | Build System & Toolchain | ![](https://img.shields.io/badge/backends-CMake%20%7C%20Meson-orange) |

### 🟣 AI & Neural

| | Repo | Description | Stats |
|---|------|-------------|-------|
| 🧠 | [**eAI**](https://github.com/embeddedos-org/eAI) | Embedded AI & TinyML | ![](https://img.shields.io/badge/runtime-TFLite%20%7C%20ONNX-purple) ![](https://img.shields.io/badge/LoRA-fine--tune-pink) |
| 🧬 | [**eNI**](https://github.com/embeddedos-org/eNI) | Neural Interface Platform | ![](https://img.shields.io/badge/BCI-1024ch-pink) ![](https://img.shields.io/badge/EEG-30kHz-purple) |
| 🤖 | [**eVera**](https://github.com/embeddedos-org/eVera) | AI Assistant & 3D Avatar | ![](https://img.shields.io/badge/agent-ReAct-pink) ![](https://img.shields.io/badge/3D-Three.js-cyan) |

### 🟢 Apps & Services

| | Repo | Description | Stats |
|---|------|-------------|-------|
| 📱 | [**eApps**](https://github.com/embeddedos-org/eApps) | App Framework & Marketplace | ![](https://img.shields.io/badge/apps-60+-yellow) ![](https://img.shields.io/badge/LVGL-widgets-green) |
| 🗄 | [**eDB**](https://github.com/embeddedos-org/eDB) | Multi-Model Database | ![](https://img.shields.io/badge/models-SQL%20%7C%20Doc%20%7C%20Graph%20%7C%20KV-green) |
| 🌐 | [**eBrowser**](https://github.com/embeddedos-org/eBrowser) | Embedded Web Browser | ![](https://img.shields.io/badge/HTML5-CSS3-cyan) ![](https://img.shields.io/badge/TLS-1.3-blue) |
| 📄 | [**eOffice**](https://github.com/embeddedos-org/eOffice) | AI Office Suite | ![](https://img.shields.io/badge/collab-CRDT-orange) ![](https://img.shields.io/badge/formats-OOXML%20%7C%20ODF-blue) |
| 📈 | [**eStocks**](https://github.com/embeddedos-org/eStocks_Trading_Scripts) | Algorithmic Trading | ![](https://img.shields.io/badge/backtest-walk--forward-blue) ![](https://img.shields.io/badge/risk-VaR-red) |

### 🟠 Tools & Hardware

| | Repo | Description | Stats |
|---|------|-------------|-------|
| 🔬 | [**EoSim**](https://github.com/embeddedos-org/EoSim) | Hardware Simulator | ![](https://img.shields.io/badge/QEMU-Renode-red) ![](https://img.shields.io/badge/platforms-52+-orange) |
| 🎨 | [**EoStudio**](https://github.com/embeddedos-org/EoStudio) | IDE & Design Suite | ![](https://img.shields.io/badge/editors-12-purple) ![](https://img.shields.io/badge/LSP-Tree--sitter-blue) |
| 🔩 | [**eHardware**](https://github.com/embeddedos-org/eHardware-Designs-Products) | Hardware Designs | ![](https://img.shields.io/badge/KiCad-PCB-green) ![](https://img.shields.io/badge/products-3-orange) |

---

## 📚 Book Library — EmbeddedOS Press

<div align="center">

**16 professional reference books** with colorful covers, architecture diagrams, 3D visuals, and academic citations. Free PDF downloads.

| | | | |
|:---:|:---:|:---:|:---:|
| <a href="https://github.com/embeddedos-org/eos/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eos/master/docs/book/cover.png" width="120"><br><b>EoS</b></a> | <a href="https://github.com/embeddedos-org/eBoot/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eBoot/master/docs/book/cover.png" width="120"><br><b>eBoot</b></a> | <a href="https://github.com/embeddedos-org/ebuild/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/ebuild/master/docs/book/cover.png" width="120"><br><b>ebuild</b></a> | <a href="https://github.com/embeddedos-org/eIPC/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eIPC/master/docs/book/cover.png" width="120"><br><b>eIPC</b></a> |
| <a href="https://github.com/embeddedos-org/eAI/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eAI/master/docs/book/cover.png" width="120"><br><b>eAI</b></a> | <a href="https://github.com/embeddedos-org/eNI/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eNI/master/docs/book/cover.png" width="120"><br><b>eNI</b></a> | <a href="https://github.com/embeddedos-org/EoSim/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/EoSim/master/docs/book/cover.png" width="120"><br><b>EoSim</b></a> | <a href="https://github.com/embeddedos-org/EoStudio/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/EoStudio/master/docs/book/cover.png" width="120"><br><b>EoStudio</b></a> |
| <a href="https://github.com/embeddedos-org/eApps/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eApps/master/docs/book/cover.png" width="120"><br><b>eApps</b></a> | <a href="https://github.com/embeddedos-org/eDB/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eDB/master/docs/book/cover.png" width="120"><br><b>eDB</b></a> | <a href="https://github.com/embeddedos-org/eBrowser/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eBrowser/master/docs/book/cover.png" width="120"><br><b>eBrowser</b></a> | <a href="https://github.com/embeddedos-org/eOffice/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eOffice/master/docs/book/cover.png" width="120"><br><b>eOffice</b></a> |
| <a href="https://github.com/embeddedos-org/eVera/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eVera/master/docs/book/cover.png" width="120"><br><b>eVera</b></a> | <a href="https://github.com/embeddedos-org/eStocks_Trading_Scripts/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eStocks_Trading_Scripts/master/docs/book/cover.png" width="120"><br><b>eStocks</b></a> | <a href="https://github.com/embeddedos-org/eHardware-Designs-Products/releases"><img src="https://raw.githubusercontent.com/embeddedos-org/eHardware-Designs-Products/master/docs/book/cover.png" width="120"><br><b>eHardware</b></a> | <a href="https://embeddedos-org.github.io/books.html"><img src="https://raw.githubusercontent.com/embeddedos-org/embeddedos-org.github.io/master/docs/book/cover.png" width="120"><br><b>Ecosystem</b></a> |

[**📚 Browse All Books →**](https://embeddedos-org.github.io/books.html)

</div>

---

## 🖥 Supported Hardware

| | Target | Architecture | Vendor / SoC | Class |
|---|--------|-------------|-------------|-------|
| 💠 | `stm32f4` | ARM Cortex-M4 | ST STM32F407 | MCU |
| 💠 | `stm32h7` | ARM Cortex-M7 | ST STM32H743 | MCU |
| 💠 | `nrf52` | ARM Cortex-M4F | Nordic nRF52840 | MCU |
| 💠 | `rp2040` | ARM Cortex-M0+ | RPi RP2040 | MCU |
| 🟢 | `raspi4` | AArch64 | Broadcom BCM2711 | SBC |
| 🟢 | `imx8m` | AArch64 | NXP i.MX8M | SoC |
| 🔴 | `riscv_virt` | RISC-V 64 | EoSim virt | Virtual |
| 🔴 | `sifive_u` | RISC-V 64 | SiFive FU740 | SBC |
| 🟠 | `esp32` | Xtensa LX6 | Espressif ESP32 | MCU |
| 🔵 | `x86_64` | x86_64 | Generic EFI PC | PC |

> **83 total board ports** across ARM Cortex-M, Cortex-A, RISC-V, x86_64, Xtensa, MIPS, and PowerPC

---

## ⚡ Quick Start

```bash
# 🔧 Build the OS
git clone https://github.com/embeddedos-org/eos.git && cd eos
cmake -B build -DEOS_PRODUCT=robot -DEOS_BUILD_TESTS=ON
cmake --build build && ctest --test-dir build

# 🔐 Build the bootloader
git clone https://github.com/embeddedos-org/eBoot.git && cd eBoot
cmake -B build -DEBLDR_BOARD=stm32f4 && cmake --build build

# 🔬 Run the simulator
pip install eosim && eosim run stm32f4 --timeout 30

# 🏪 Browse the App Store
open https://embeddedos-org.github.io/eApps/
```

---

## 🔄 CI/CD Pipeline

| Workflow | Schedule | Purpose |
|----------|----------|---------|
| 🔵 **CI** | Every push/PR | Build + test on Linux × Windows × macOS |
| 🌙 **Nightly** | 2:00 AM UTC | Full regression across all platforms |
| 📅 **Weekly** | Monday 6 AM | Dependency audit + comprehensive build |
| 🔬 **Simulation** | 3:00 AM UTC | QEMU/EoSim validation (7+ architectures) |
| 📦 **Release** | Tag-triggered | Build + test + PDF book + GitHub Release |
| 📚 **Book Build** | docs/book/** push | pandoc 3.6 + Eisvogel → PDF auto-release |

---

## 📜 Standards & Compliance

| Category | Standards |
|----------|----------|
| 🏗 Systems | ISO/IEC/IEEE 15288, ISO 12207, IEEE 42010 |
| ✅ Quality | ISO 25000/25010, IEEE 29119, ISO 9001 |
| 🔒 Security | ISO 27001, FIPS 140-3, ISO 15408 |
| ⚠️ Safety | IEC 61508, ISO 26262, DO-178C |
| 📋 Supply Chain | SBOM (SPDX, CycloneDX), OpenChain |

---

<div align="center">

**MIT License** · Made with ❤️ by [Srikanth Patchava](https://github.com/embeddedos-org) & Contributors

[🌐 Website](https://embeddedos-org.github.io) · [📚 Books](https://embeddedos-org.github.io/books.html) · [🏪 Apps](https://embeddedos-org.github.io/eApps/) · [⭐ Star us on GitHub](https://github.com/embeddedos-org/eos)

</div>
