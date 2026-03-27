# Contributing to the EoS Platform

Thank you for your interest in contributing to the EoS ecosystem! This guide covers development setup for all seven repositories and the conventions we follow.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Repository Overview](#repository-overview)
- [Prerequisites](#prerequisites)
- [Development Setup](#development-setup)
  - [eos — Embedded OS](#eos--embedded-os)
  - [eboot — Bootloader](#eboot--bootloader)
  - [ebuild — Build System](#ebuild--build-system)
  - [eipc — Embedded IPC](#eipc--embedded-ipc)
  - [eai — AI Layer](#eai--ai-layer)
  - [eni — Neural Interface](#eni--neural-interface)
  - [eos-sdk — Unified SDK](#eos-sdk--unified-sdk)
- [Workflow](#workflow)
- [Commit Message Convention](#commit-message-convention)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Issue Reporting](#issue-reporting)
- [License](#license)

---

## Code of Conduct

We are committed to providing a welcoming and inclusive experience for everyone. Be respectful, constructive, and professional in all interactions. Harassment, discrimination, and disruptive behavior will not be tolerated.

---

## Repository Overview

| Repository | Language | Build System | Description |
|------------|----------|-------------|-------------|
| [eos](https://github.com/embeddedos-org/eos) | C | CMake | Embedded OS — HAL, kernel, services, 41 product profiles |
| [eboot](https://github.com/embeddedos-org/eboot) | C | CMake | Bootloader — 24 boards, secure boot, A/B OTA |
| [ebuild](https://github.com/embeddedos-org/ebuild) | Python | pip/setuptools | Build system — 10 backends, package manager, AI analyzer |
| [eipc](https://github.com/embeddedos-org/eipc) | Go + C | Go modules + CMake | IPC framework — security, transports, services |
| [eai](https://github.com/embeddedos-org/eai) | C | CMake | AI layer — edge agents, industrial AI, connectors |
| [eni](https://github.com/embeddedos-org/eni) | C | CMake | Neural interface — BCI, assistive input, policy engine |
| [eos-sdk](https://github.com/embeddedos-org/eos-sdk) | C | CMake | Unified SDK — single header, feature-flag driven |

---

## Prerequisites

### All Projects

- **Git** 2.30+
- A GitHub account with fork access

### C Projects (eos, eboot, eai, eni, eos-sdk)

| Tool | Version | Purpose |
|------|---------|---------|
| GCC or Clang | 10+ | C compiler |
| CMake | 3.15+ | Build system generator |
| Make or Ninja | Any | Build tool |
| CTest | (bundled with CMake) | Test runner |

### Cross-Compilation (eboot board ports)

| Tool | Purpose |
|------|---------|
| `gcc-arm-none-eabi` | ARM Cortex-M targets |
| `gcc-aarch64-linux-gnu` | ARM64 Cortex-A targets |
| `gcc-riscv64-linux-gnu` | RISC-V targets |

### Python Projects (ebuild)

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.9+ | Runtime |
| pip | Latest | Package installer |
| flake8, black, isort | Latest | Linting and formatting |

### Go Projects (eipc)

| Tool | Version | Purpose |
|------|---------|---------|
| Go | 1.21+ | Compiler and toolchain |
| golangci-lint | Latest | Linting |

### Platform-Specific Setup

<details>
<summary><b>🐧 Linux (Ubuntu / Debian)</b></summary>

```bash
sudo apt update
sudo apt install -y \
  git build-essential cmake ninja-build \
  python3 python3-pip python3-venv \
  golang-go \
  gcc-arm-none-eabi gcc-aarch64-linux-gnu gcc-riscv64-linux-gnu
```
</details>

<details>
<summary><b>🐧 Linux (Fedora / RHEL)</b></summary>

```bash
sudo dnf install -y \
  git gcc gcc-c++ cmake ninja-build \
  python3 python3-pip \
  golang \
  arm-none-eabi-gcc-cs
```
</details>

<details>
<summary><b>🍎 macOS</b></summary>

```bash
brew install cmake ninja python go
brew install --cask gcc-arm-embedded
```
</details>

<details>
<summary><b>🪟 Windows</b></summary>

```powershell
# Install via winget
winget install Kitware.CMake
winget install Ninja-build.Ninja
winget install Python.Python.3.12
winget install GoLang.Go

# Or use WSL (recommended for cross-compilation)
wsl --install -d Ubuntu
```
</details>

---

## Development Setup

### Clone All Repositories

```bash
# Create workspace
mkdir -p ~/EoS && cd ~/EoS

# Clone all repos
for repo in eos eboot ebuild eipc eai eni eos-sdk; do
  git clone https://github.com/embeddedos-org/$repo.git
done
```

---

### eos — Embedded OS

```bash
cd ~/EoS/eos

# Build with tests
cmake -B build -DEOS_BUILD_TESTS=ON
cmake --build build
ctest --test-dir build --output-on-failure

# Build for a specific product profile
cmake -B build -DEOS_PRODUCT=robot -DEOS_BUILD_TESTS=ON
cmake --build build

# Build with ebuild (if installed)
ebuild build
```

**Key directories:**

| Path | What to edit |
|------|-------------|
| `hal/src/` | HAL implementations (add peripherals here) |
| `hal/include/eos/` | HAL public headers |
| `kernel/src/` | RTOS kernel (tasks, sync, IPC, multicore) |
| `services/` | Crypto, OTA, sensor, motor, filesystem, networking |
| `products/` | Product profile headers (41 profiles) |
| `include/eos/eos_config.h` | Master config with `EOS_ENABLE_*` flags |
| `tests/` | Unit tests (8 test suites) |

**Test suites:**

```bash
ctest --test-dir build -R test_hal         # HAL tests
ctest --test-dir build -R test_kernel      # Kernel tests
ctest --test-dir build -R test_crypto      # Crypto tests
ctest --test-dir build -R test_multicore   # Multicore tests
```

---

### eboot — Bootloader

```bash
cd ~/EoS/eboot

# Native build (core libraries + tests, no board-specific code)
cmake -B build -DEBLDR_BUILD_TESTS=ON
cmake --build build
ctest --test-dir build --output-on-failure

# Cross-compile for a specific board
cmake -B build -DEBLDR_BOARD=stm32f4 \
  -DCMAKE_TOOLCHAIN_FILE=toolchains/arm-none-eabi.cmake
cmake --build build
```

**Key directories:**

| Path | What to edit |
|------|-------------|
| `core/` | Platform-agnostic boot logic (bootctl, crypto, firmware update) |
| `include/` | Public headers (22 service APIs) |
| `hal/` | HAL dispatch + board registry |
| `stage0/` | Minimal first-stage bootloader |
| `stage1/` | Full boot manager |
| `boards/` | Board ports (24 platforms — add new boards here) |
| `tests/` | Unit tests (7 test suites) |
| `configs/` | Boot config schemas (YAML) |

**Adding a new board:**

1. Create `boards/<name>/board_<name>.h` — memory map and constants
2. Create `boards/<name>/board_<name>.c` — implement `eos_board_ops_t`
3. Add `eboot_add_board()` in `CMakeLists.txt`
4. Add linker scripts if needed

---

### ebuild — Build System

```bash
cd ~/EoS/ebuild

# Install in development mode
pip install -e .

# Verify
ebuild --version
ebuild --help

# Run tests
python -m pytest tests/ -v

# Run the full pipeline test
python test_full_pipeline.py

# Run EoS AI tests
python tests/test_eos_ai.py

# Lint
flake8 ebuild/
black --check ebuild/
isort --check ebuild/
```

**Key directories:**

| Path | What to edit |
|------|-------------|
| `ebuild/cli/` | CLI commands (Click-based) |
| `ebuild/core/` | Config parser, dependency graph |
| `ebuild/build/` | Build dispatch + backends |
| `ebuild/build/backends/` | Individual backend wrappers (cmake, make, cargo, etc.) |
| `ebuild/packages/` | Package manager (recipes, resolver, fetcher, cache) |
| `ebuild/system/` | Linux system image builder |
| `ebuild/firmware/` | RTOS firmware builder + flash tools |
| `ebuild/eos_ai/` | Hardware design analyzer |
| `recipes/` | Package recipes (YAML) |
| `templates/` | Project templates |

**Adding a new build backend:**

1. Create `ebuild/build/backends/<name>_backend.py`
2. Implement the backend interface (configure, build, clean, install)
3. Register in `ebuild/build/dispatch.py`
4. Add auto-detection rules (file patterns)
5. Add tests in `tests/`

---

### eipc — Embedded IPC

```bash
cd ~/EoS/eipc

# Build Go components
go build ./...

# Run Go tests
go test ./... -v

# Run integration tests
go test ./tests/ -v -tags=integration

# Build C SDK
cd sdk/c
cmake -B build
cmake --build build
ctest --test-dir build --output-on-failure

# Lint Go code
golangci-lint run ./...
```

**Key directories:**

| Path | What to edit |
|------|-------------|
| `core/` | Message types, router, endpoint (Go) |
| `protocol/` | Frame format, codec, headers (Go) |
| `security/` | Auth, capabilities, HMAC, replay, keyring (Go) |
| `transport/` | Unix, TCP, shared memory, Windows pipes (Go) |
| `services/` | Broker, policy, audit, registry, health (Go) |
| `cmd/` | CLI binaries (eipc-client, eipc-server) |
| `sdk/c/` | C SDK for embedded integration |
| `sdk/c/include/` | C public headers (`eipc.h`, `eipc_types.h`) |

**Adding a new transport:**

1. Create `transport/<name>/<name>.go`
2. Implement the `transport.Transport` interface
3. Add tests in `transport/<name>/<name>_test.go`
4. Register in transport factory

---

### eai — AI Layer

```bash
cd ~/EoS/eai

# Build with tests
cmake -B build -DEAI_BUILD_TESTS=ON
cmake --build build
ctest --test-dir build --output-on-failure
```

**Key directories:**

| Path | What to edit |
|------|-------------|
| `common/` | Shared contracts: types, config, manifest, tools, security |
| `min/` | EAI-Min: lightweight agent, router, runtime (llama.cpp) |
| `framework/` | EAI-Framework: orchestrator, connectors, policy, observability |
| `platform/` | Platform adapters (EoS, Linux, Windows) |
| `profiles/` | Deployment profiles (YAML) |
| `cli/` | CLI entry point |

**Adding a new connector (EAI-Framework):**

1. Create `framework/src/connector_<name>.c`
2. Add header in `framework/include/eai_fw/connector.h`
3. Register in connector factory
4. Add a deployment profile in `profiles/`

---

### eni — Neural Interface

```bash
cd ~/EoS/eni

# Build with tests
cmake -B build -DENI_BUILD_TESTS=ON
cmake --build build
ctest --test-dir build --output-on-failure
```

**Key directories:**

| Path | What to edit |
|------|-------------|
| `common/` | Shared types, events, policy, tool calls, EIPC bridge |
| `min/` | ENI-Min: input adapter, normalizer, mapper, policy filter |
| `framework/` | ENI-Framework: provider manager, stream bus, router, orchestrator |
| `platform/` | Platform adapters (EoS, Linux, Windows) |
| `providers/` | Input providers (simulator, generic decoder) |

**Adding a new provider:**

1. Create `providers/<name>/<name>.c` and `<name>.h`
2. Implement the provider contract from `common/include/eni/provider_contract.h`
3. Register in provider manager
4. Add tests in `tests/`

---

### eos-sdk — Unified SDK

```bash
cd ~/EoS/eos-sdk

# Build with examples and tests
cmake -B build \
  -DEOS_SDK_BUILD_EXAMPLES=ON \
  -DEOS_SDK_BUILD_TESTS=ON \
  -DEOS_SDK_FETCH_DEPS=OFF  # Use local repos instead of fetching
cmake --build build
ctest --test-dir build --output-on-failure

# Build with specific packages disabled
cmake -B build \
  -DEOS_SDK_ENABLE_OS=ON \
  -DEOS_SDK_ENABLE_BOOT=ON \
  -DEOS_SDK_ENABLE_IPC=OFF \
  -DEOS_SDK_ENABLE_ENI=OFF \
  -DEOS_SDK_ENABLE_AI=OFF
cmake --build build
```

**Key directories:**

| Path | What to edit |
|------|-------------|
| `include/eos_sdk.h` | Unified header with feature-flag includes |
| `src/eos_sdk.c` | SDK lifecycle (init, version, info) |
| `examples/` | Example applications |
| `cmake/` | CMake config and pkg-config templates |

---

## Workflow

### 1. Fork and Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/<your-username>/<repo>.git
cd <repo>
git remote add upstream https://github.com/embeddedos-org/<repo>.git
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

Branch naming conventions:

| Prefix | Use for |
|--------|---------|
| `feature/` | New features |
| `fix/` | Bug fixes |
| `docs/` | Documentation changes |
| `refactor/` | Code restructuring |
| `test/` | Test additions or fixes |

### 3. Make Changes

- Follow the [Coding Standards](#coding-standards) below
- Write tests for new functionality
- Keep commits focused and atomic

### 4. Test

```bash
# C projects
cmake --build build && ctest --test-dir build --output-on-failure

# Python (ebuild)
python -m pytest tests/ -v && flake8 ebuild/ && black --check ebuild/

# Go (eipc)
go test ./... -v && golangci-lint run
```

### 5. Push and Submit PR

```bash
git push origin feature/your-feature-name
```

Open a Pull Request on GitHub against the `main` branch.

---

## Commit Message Convention

```
<type>(<scope>): <short description>

<optional body>
```

### Types

| Type | When to use |
|------|------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, no code change |
| `refactor` | Restructure without behavior change |
| `test` | Add or fix tests |
| `build` | Build system or dependency changes |
| `ci` | CI/CD pipeline changes |
| `perf` | Performance improvement |

### Scope (optional)

Use the module name: `hal`, `kernel`, `bootctl`, `crypto`, `cli`, `cmake`, `transport`, etc.

### Examples

```
feat(hal): add radar peripheral interface
fix(bootctl): correct CRC calculation for slot B
docs(eni): add provider integration guide
test(eipc): add shared memory transport tests
build(ebuild): add NuttX backend auto-detection
```

---

## Pull Request Guidelines

### Before Submitting

- [ ] Code compiles without warnings (`-Wall -Wextra -Werror` for C)
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Documentation updated if API changed
- [ ] Commit messages follow the convention above
- [ ] Branch is rebased on latest `main`

### PR Description Template

```markdown
## Summary
Brief description of what this PR does.

## Changes
- Change 1
- Change 2

## Testing
How was this tested? Which test suites were run?

## Related Issues
Closes #XX (if applicable)
```

### Review Process

1. At least one maintainer approval required
2. CI must pass (build + tests on Linux/Windows/macOS)
3. No merge conflicts with `main`

---

## Coding Standards

### C (eos, eboot, eai, eni, eos-sdk)

- **Standard:** C11
- **Style:** 4-space indentation, `snake_case` for functions and variables
- **Prefixes:** `eos_` for eos, `eboot_`/`eos_` for eboot, `eai_` for eai, `eni_` for eni
- **Headers:** Include guards (`#ifndef FOO_H` / `#define FOO_H` / `#endif`)
- **Comments:** Doxygen-style for public APIs (`/** @brief ... */`)
- **Warnings:** Code must compile clean with `-Wall -Wextra -Werror`

```c
/**
 * @brief Initialize the sensor subsystem.
 * @param config Sensor configuration.
 * @return 0 on success, negative error code on failure.
 */
int eos_sensor_init(const eos_sensor_config_t *config);
```

### Python (ebuild)

- **Style:** PEP 8, enforced by `black` and `isort`
- **Line length:** 88 characters (black default)
- **Type hints:** Encouraged for public functions
- **Docstrings:** Google style

```python
def build(backend: str, config: BuildConfig) -> int:
    """Build the project using the specified backend.

    Args:
        backend: Build backend name (cmake, make, cargo, etc.).
        config: Build configuration from build.yaml.

    Returns:
        Exit code (0 for success).
    """
```

### Go (eipc)

- **Style:** `gofmt` / `goimports` (standard Go formatting)
- **Linting:** `golangci-lint`
- **Comments:** GoDoc style for exported types and functions
- **Error handling:** Always check and return errors, no panics in library code

```go
// Send transmits a message to the connected endpoint.
// Returns an error if the connection is closed or the message is invalid.
func (e *Endpoint) Send(msg Message) error {
```

---

## Testing

### Test Coverage Expectations

| Project | Minimum Coverage | Focus Areas |
|---------|-----------------|-------------|
| eos | Core HAL, kernel, crypto | Platform-agnostic logic |
| eboot | Boot control, crypto, firmware update | All 7 test suites |
| ebuild | CLI commands, backends, AI analyzer | Pipeline integration |
| eipc | Protocol, security, transports | Integration tests |
| eai | Common contracts, min runtime | Tool execution, policy |
| eni | Input pipeline, policy filter | Event flow, providers |
| eos-sdk | SDK init, feature flags | Compile-time selection |

### Writing Tests

**C projects** use CTest with simple assertion macros:

```c
void test_sha256_known_vector(void) {
    uint8_t hash[32];
    eos_sha256("abc", 3, hash);
    assert(memcmp(hash, expected_hash, 32) == 0);
    printf("PASS: test_sha256_known_vector\n");
}
```

**Python** uses pytest:

```python
def test_cmake_backend_detect():
    assert detect_backend("/path/with/CMakeLists.txt") == "cmake"
```

**Go** uses standard `testing` package:

```go
func TestEndpointSend(t *testing.T) {
    ep := NewEndpoint("unix", "/tmp/test.sock")
    err := ep.Send(Message{Type: "intent"})
    if err != nil {
        t.Fatalf("Send failed: %v", err)
    }
}
```

---

## Issue Reporting

### Bug Reports

[Open an issue](https://github.com/embeddedos-org) on the relevant repository with:

- **Title:** Clear, concise description
- **Environment:** OS, compiler version, board (if applicable)
- **Steps to reproduce:** Minimal sequence to trigger the bug
- **Expected behavior:** What should happen
- **Actual behavior:** What actually happens
- **Logs/output:** Relevant error messages or build output

### Feature Requests

- **Describe the use case** — what problem does this solve?
- **Proposed solution** — how should it work?
- **Alternatives considered** — other approaches you thought about
- **Which repo** — where should this be implemented?

---

## License

All contributions are made under the **MIT License**. By submitting a pull request, you agree that your contribution will be licensed under the same terms.

---

## Questions?

- Open a [Discussion](https://github.com/orgs/embeddedos-org/discussions) for general questions
- File an [Issue](https://github.com/embeddedos-org) for bugs or feature requests
- Check individual repo READMEs for project-specific details

Thank you for contributing to the EoS Platform! 🚀
