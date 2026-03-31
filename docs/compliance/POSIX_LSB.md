# EoS POSIX & Linux Standard Base Compliance

> **Document**: POSIX_LSB.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document covers EoS alignment with POSIX (IEEE 1003.1) and Linux Standard Base (LSB) standards, mapping standard APIs and filesystem conventions to EoS implementation.

---

## Table of Contents

1. [Overview](#1-overview)
2. [POSIX — IEEE 1003.1](#2-posix--ieee-10031)
3. [POSIX System Interfaces](#3-posix-system-interfaces)
4. [POSIX Compatibility Layer](#4-posix-compatibility-layer)
5. [Linux Standard Base](#5-linux-standard-base)
6. [LSB Filesystem Hierarchy](#6-lsb-filesystem-hierarchy)
7. [EoS Linux HAL Backend](#7-eos-linux-hal-backend)
8. [Compliance Matrix](#8-compliance-matrix)

---

## 1. Overview

EoS provides a POSIX compatibility layer enabling portable application development across EoS bare-metal, RTOS, and Linux-backed configurations. When running on Linux-capable hardware, EoS additionally aligns with the Linux Standard Base for filesystem layout, packaging, and shared library management.

### Architecture

```
┌──────────────────────────────┐
│   POSIX Application          │  examples/posix-app
├──────────────────────────────┤
│   POSIX Compatibility Layer  │  eos/posix/
├──────────────────────────────┤
│   EoS Kernel / HAL           │  eos/core/, eos/hal/
├──────────────────────────────┤
│   Hardware / Linux Host      │  hal_linux.c / bare-metal
└──────────────────────────────┘
```

---

## 2. POSIX — IEEE 1003.1

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | IEEE 1003.1-2017 (POSIX.1-2017) |
| **Full Name** | Portable Operating System Interface |
| **Also Known As** | The Open Group Base Specifications Issue 7 (2018 edition) |
| **Scope** | System interfaces, shell and utilities, real-time extensions |
| **EoS Target** | POSIX.1 system interfaces subset for embedded use |

### POSIX Conformance Levels

| Level | Description | EoS Status |
|-------|-------------|:----------:|
| **POSIX.1 Core** | Base system interfaces (file I/O, processes, signals) | ✅ Supported |
| **POSIX.1 Realtime** | Semaphores, timers, message queues, shared memory | ✅ Supported |
| **POSIX.1 Threads** | pthreads, mutexes, condition variables, barriers | ✅ Supported |
| **POSIX.1 Advanced Realtime** | Typed memory, spawn, clock selection | 🔶 Partial |
| **POSIX.2 Shell & Utilities** | sh, awk, grep, sed, make | 📋 Planned (via BusyBox) |

---

## 3. POSIX System Interfaces

### Thread Management (pthreads)

| POSIX API | EoS Implementation | Status |
|-----------|---------------------|:------:|
| `pthread_create()` | Maps to EoS task creation | ✅ |
| `pthread_join()` | Task join with return value | ✅ |
| `pthread_detach()` | Detached task mode | ✅ |
| `pthread_exit()` | Task termination | ✅ |
| `pthread_self()` | Current task handle | ✅ |
| `pthread_cancel()` | Task cancellation with cleanup | ✅ |
| `pthread_attr_*()` | Stack size, priority, scheduling | ✅ |

### Synchronization Primitives

| POSIX API | EoS Implementation | Status |
|-----------|---------------------|:------:|
| `pthread_mutex_init/lock/unlock/destroy()` | EoS mutex wrapper | ✅ |
| `pthread_cond_init/wait/signal/broadcast()` | EoS condition variable | ✅ |
| `pthread_rwlock_*()` | Read-write lock | ✅ |
| `pthread_barrier_*()` | Barrier synchronization | ✅ |
| `pthread_spin_*()` | Spinlock | ✅ |

### Semaphores

| POSIX API | EoS Implementation | Status |
|-----------|---------------------|:------:|
| `sem_init()` | Unnamed semaphore (count-based) | ✅ |
| `sem_wait()` | Blocking decrement | ✅ |
| `sem_trywait()` | Non-blocking decrement | ✅ |
| `sem_timedwait()` | Timed wait with `timespec` | ✅ |
| `sem_post()` | Increment (signal) | ✅ |
| `sem_getvalue()` | Current count query | ✅ |
| `sem_open()` | Named semaphore | 🔶 Partial |
| `sem_unlink()` | Named semaphore removal | 🔶 Partial |

### Signals

| POSIX API | EoS Implementation | Status |
|-----------|---------------------|:------:|
| `signal()` | Basic signal handler registration | ✅ |
| `sigaction()` | Advanced signal handling with flags | ✅ |
| `kill()` | Send signal to task | ✅ |
| `sigprocmask()` | Signal blocking mask | ✅ |
| `sigwait()` | Synchronous signal wait | ✅ |
| `sigsuspend()` | Atomic unmask + suspend | ✅ |
| `SIGINT, SIGTERM, SIGUSR1/2` | Standard signal set | ✅ |
| `SIGRTMIN–SIGRTMAX` | Real-time signals | 🔶 Partial |

### File I/O

| POSIX API | EoS Implementation | Status |
|-----------|---------------------|:------:|
| `open()` / `close()` | VFS file descriptor management | ✅ |
| `read()` / `write()` | Synchronous I/O | ✅ |
| `lseek()` | File position | ✅ |
| `stat()` / `fstat()` | File metadata | ✅ |
| `mkdir()` / `rmdir()` | Directory management | ✅ |
| `opendir()` / `readdir()` | Directory traversal | ✅ |
| `unlink()` | File removal | ✅ |
| `rename()` | File renaming | ✅ |
| `fcntl()` | File control (flags, locks) | 🔶 Partial |
| `mmap()` / `munmap()` | Memory-mapped I/O | 🔶 Partial (Linux backend) |
| `aio_read()` / `aio_write()` | Asynchronous I/O | 📋 Planned |

### Sockets

| POSIX API | EoS Implementation | Status |
|-----------|---------------------|:------:|
| `socket()` | AF_INET, AF_INET6, AF_UNIX | ✅ |
| `bind()` / `listen()` / `accept()` | Server socket lifecycle | ✅ |
| `connect()` | Client connection | ✅ |
| `send()` / `recv()` | Stream I/O | ✅ |
| `sendto()` / `recvfrom()` | Datagram I/O | ✅ |
| `select()` | Synchronous I/O multiplexing | ✅ |
| `poll()` | Pollable I/O multiplexing | ✅ |
| `epoll_*()` | Linux-specific (non-POSIX) | ✅ (Linux backend only) |
| `getaddrinfo()` | DNS resolution | ✅ (Linux backend only) |

### Clocks and Timers

| POSIX API | EoS Implementation | Status |
|-----------|---------------------|:------:|
| `clock_gettime()` | Monotonic and realtime clocks | ✅ |
| `clock_nanosleep()` | High-resolution sleep | ✅ |
| `timer_create()` | Per-process timers | ✅ |
| `timer_settime()` | Timer arming with interval | ✅ |
| `nanosleep()` | Thread sleep | ✅ |
| `usleep()` | Microsecond sleep | ✅ |

---

## 4. POSIX Compatibility Layer

### Implementation Architecture

The EoS POSIX layer translates POSIX calls into native EoS kernel primitives:

| POSIX Concept | EoS Kernel Primitive | Translation |
|---------------|---------------------|-------------|
| pthread | EoS task (TCB) | 1:1 mapping |
| mutex | EoS mutex (priority inheritance) | Direct wrapper |
| semaphore | EoS counting semaphore | Direct wrapper |
| signal | EoS event flags + ISR hooks | Emulated |
| file descriptor | EoS VFS fd table | Direct wrapper |
| socket | EoS network stack / Linux passthrough | Backend-dependent |

### Example: POSIX Application on EoS

The `examples/posix-app` directory demonstrates a portable POSIX application:

```c
// SPDX-License-Identifier: MIT
#include <pthread.h>
#include <semaphore.h>
#include <signal.h>
#include <stdio.h>

static sem_t data_ready;
static volatile sig_atomic_t running = 1;

void sig_handler(int sig) { running = 0; }

void *worker(void *arg) {
    while (running) {
        sem_wait(&data_ready);
        printf("Worker: processing data\n");
    }
    return NULL;
}

int main(void) {
    signal(SIGINT, sig_handler);
    sem_init(&data_ready, 0, 0);

    pthread_t tid;
    pthread_create(&tid, NULL, worker, NULL);

    for (int i = 0; i < 5 && running; i++) {
        sem_post(&data_ready);
        usleep(100000);
    }

    running = 0;
    sem_post(&data_ready);
    pthread_join(tid, NULL);
    sem_destroy(&data_ready);
    return 0;
}
```

### Build Targets

| Target | Backend | POSIX Layer |
|--------|---------|-------------|
| EoS bare-metal (Cortex-M) | Native EoS kernel | POSIX shim over EoS primitives |
| EoS Linux (x86_64, ARM64) | `hal_linux.c` | Direct Linux syscalls |
| QEMU simulation | EoS kernel on QEMU | POSIX shim over EoS primitives |

---

## 5. Linux Standard Base

### Standard Reference

| Attribute | Detail |
|-----------|--------|
| **Standard** | LSB 5.0 |
| **Full Name** | Linux Standard Base |
| **Organization** | The Linux Foundation |
| **Scope** | Binary compatibility between Linux distributions |
| **EoS Applicability** | EoS Linux-backend deployments (x86_64, ARM64, RISC-V) |

### LSB Core Components

| LSB Component | Description | EoS Support |
|---------------|-------------|:-----------:|
| **Core** | Base libraries (glibc, libstdc++), dynamic linker | ✅ |
| **Desktop** | GTK, Qt, X11 libraries | N/A (embedded) |
| **Languages** | Python, Perl interpreters | 🔶 Partial (Python only) |
| **Imaging** | Printing, scanning libraries | N/A (embedded) |
| **Trial Use** | Emerging specifications | N/A |

---

## 6. LSB Filesystem Hierarchy

### Filesystem Hierarchy Standard (FHS) — EoS Mapping

| FHS Path | Purpose | EoS Usage |
|----------|---------|-----------|
| `/bin` | Essential user commands | EoS CLI tools, shell |
| `/sbin` | System administration commands | EoS system services |
| `/etc` | Host-specific configuration | EoS product config, network config |
| `/lib` | Essential shared libraries | EoS shared libs, kernel modules |
| `/usr` | Secondary hierarchy | EoS applications, development tools |
| `/usr/bin` | User commands | eApps CLI, ebuild-tool |
| `/usr/lib` | Libraries | EoS SDK libraries |
| `/usr/share` | Architecture-independent data | Documentation, eosim data |
| `/var` | Variable data | Logs, runtime state, package cache |
| `/var/log` | Log files | EoS audit logs |
| `/tmp` | Temporary files | Runtime temporary storage |
| `/dev` | Device files | EoS HAL device nodes |
| `/proc` | Process information | EoS process info (Linux backend) |
| `/sys` | Kernel/device information | Hardware info (Linux backend) |
| `/opt` | Add-on packages | Third-party EoS applications |
| `/home` | User home directories | N/A (typically single-user embedded) |

### EoS-Specific Directories

| Path | Purpose |
|------|---------|
| `/eos/config` | Product profile configuration |
| `/eos/keystore` | Encrypted credential storage |
| `/eos/services` | EoS system services |
| `/eos/apps` | Installed eApps applications |
| `/eos/firmware` | Firmware images for OTA |

### Packaging

| Requirement | LSB Specification | EoS Implementation |
|-------------|-------------------|---------------------|
| Package format | RPM or dpkg | ✅ `eos_pkg` manager (custom format) |
| Package metadata | Name, version, dependencies | ✅ Package manifest in `eos_pkg.h` |
| Install/remove scripts | Pre/post install hooks | ✅ Lifecycle hooks |
| Shared library versioning | SONAME convention | ✅ `libeos.so.0.1.0` |

---

## 7. EoS Linux HAL Backend

### hal_linux.c Implementation

The `hal_linux.c` backend maps EoS HAL APIs directly to Linux system calls:

| EoS HAL API | Linux Syscall | Description |
|-------------|---------------|-------------|
| `hal_gpio_init()` | `/sys/class/gpio` sysfs | GPIO pin configuration |
| `hal_gpio_read/write()` | sysfs read/write | GPIO value access |
| `hal_uart_init()` | `open("/dev/ttyS*")` | UART initialization |
| `hal_uart_read/write()` | `read()`/`write()` on fd | UART data transfer |
| `hal_spi_transfer()` | `ioctl(SPI_IOC_MESSAGE)` | SPI transaction |
| `hal_i2c_read/write()` | `ioctl(I2C_RDWR)` | I2C bus access |
| `hal_timer_start()` | `timer_create()` + `SIGALRM` | Timer with signal |
| `hal_sleep_ms()` | `nanosleep()` | Thread sleep |
| `hal_interrupt_enable()` | Signal handler + eventfd | Interrupt emulation |

### Linux Service Integration

| Service | EoS Integration | Mechanism |
|---------|-----------------|-----------|
| **systemd** | EoS services as systemd units | `.service` files in `/etc/systemd/system/` |
| **udev** | Device hotplug for EoS HAL | udev rules in `/etc/udev/rules.d/` |
| **syslog** | Audit log forwarding | `syslog()` API, journald integration |
| **NetworkManager** | Network configuration | D-Bus interface |
| **D-Bus** | IPC for desktop integration | `eipc` D-Bus transport (planned) |

---

## 8. Compliance Matrix

| Standard | Requirement | EoS Status |
|----------|-------------|------------|
| POSIX.1 — pthreads | Thread creation, join, detach, cancel | ✅ Implemented |
| POSIX.1 — mutexes | Mutex init, lock, unlock, trylock | ✅ Implemented |
| POSIX.1 — condition variables | Wait, signal, broadcast | ✅ Implemented |
| POSIX.1 — semaphores | Unnamed counting semaphores | ✅ Implemented |
| POSIX.1 — named semaphores | `sem_open()`, `sem_unlink()` | 🔶 Partial |
| POSIX.1 — signals | Signal handlers, masks, real-time signals | ✅ Implemented |
| POSIX.1 — file I/O | open, read, write, close, stat, seek | ✅ Implemented |
| POSIX.1 — directories | mkdir, rmdir, opendir, readdir | ✅ Implemented |
| POSIX.1 — sockets | TCP/UDP, AF_INET/INET6/UNIX | ✅ Implemented |
| POSIX.1 — clocks | clock_gettime, timer_create | ✅ Implemented |
| POSIX.1 — mmap | Memory-mapped file I/O | 🔶 Partial (Linux only) |
| POSIX.1 — async I/O | aio_read, aio_write | 📋 Planned |
| POSIX.2 — shell | sh, awk, grep, sed | 📋 Planned (BusyBox) |
| LSB 5.0 — FHS | Filesystem hierarchy compliance | ✅ Aligned |
| LSB 5.0 — shared libs | SONAME versioning | ✅ Implemented |
| LSB 5.0 — packaging | Package management system | ✅ eos_pkg |
| LSB 5.0 — systemd | Service unit files | ✅ Implemented |
| Linux HAL | GPIO, UART, SPI, I2C via sysfs/ioctl | ✅ hal_linux.c |
| Linux services | systemd, udev, syslog integration | ✅ Implemented |

**Legend**: ✅ Implemented | 🔶 Partial | 📋 Planned

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial POSIX and LSB compliance document |
# EoS POSIX & Linux Standard Base Compliance

> **Document**: POSIX_LSB.md
> **Version**: 0.1.0
> **Date**: 2026-03-31
> **SPDX-License-Identifier**: MIT

This document maps EoS POSIX-like APIs to IEEE 1003.1 (POSIX) and Linux Standard Base (LSB) specifications.

---

## Table of Contents

1. [Overview](#1-overview)
2. [POSIX (IEEE 1003.1)](#2-posix-ieee-10031)
3. [Linux Standard Base (LSB)](#3-linux-standard-base-lsb)
4. [EoS Compatibility Layers](#4-eos-compatibility-layers)
5. [API Mapping](#5-api-mapping)
6. [Compliance Matrix](#6-compliance-matrix)

---

## 1. Overview

EoS provides POSIX-compatible APIs through its compatibility layer in `eos/src/compat/posix/`, enabling developers familiar with POSIX systems to write portable code targeting EoS embedded platforms. While EoS is not a full POSIX-certified operating system, it implements the most commonly used POSIX interfaces for threads, synchronization, signals, and I/O.

### Relevant Repos

| Repo | POSIX Role |
|------|-----------|
| `eos` | POSIX compatibility layer implementation |
| `eos-sdk` | SDK headers exposing POSIX-like APIs |
| `eipc` | POSIX-compatible IPC mechanisms |
| `eosim` | Simulation of POSIX-compatible platforms |

---

## 2. POSIX (IEEE 1003.1)

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Full Title** | IEEE Standard for Information Technology — Portable Operating System Interface |
| **Standard** | IEEE Std 1003.1-2017 (POSIX.1-2017) |
| **Also Known As** | Single UNIX Specification (SUS) v4, The Open Group Base Specifications Issue 7 |
| **Scope** | System interfaces, shell, utilities, headers |

### EoS POSIX Implementation Scope

| POSIX Category | EoS Status | Implementation |
|---------------|:----------:|----------------|
| **Threads (pthreads)** | ✅ Implemented | `eos/src/compat/posix/eos_posix_threads.c` |
| **Mutexes** | ✅ Implemented | `pthread_mutex_init/lock/unlock/destroy` |
| **Condition Variables** | ✅ Implemented | `pthread_cond_init/wait/signal/broadcast` |
| **Read-Write Locks** | ✅ Implemented | `pthread_rwlock_*` |
| **Barriers** | ✅ Implemented | `pthread_barrier_*` |
| **Thread-Specific Data** | ✅ Implemented | `pthread_key_create/getspecific/setspecific` |
| **Semaphores** | ✅ Implemented | `sem_init/wait/post/destroy` |
| **Signals** | ✅ Implemented | `eos/src/compat/posix/eos_posix_signals.c` |
| **File I/O** | ✅ Implemented | `eos/src/compat/posix/eos_posix_io.c` |
| **Message Queues** | ✅ Implemented | `mq_open/send/receive/close` |
| **Shared Memory** | ✅ Implemented | `shm_open/mmap/munmap` |
| **Clocks & Timers** | ✅ Implemented | `clock_gettime/nanosleep/timer_*` |
| **Process Management** | ⚠️ Partial | Fork/exec not applicable to RTOS; task-based model |
| **File System** | ⚠️ Partial | Basic open/read/write/close; no full VFS |
| **Networking (sockets)** | 📋 Planned | TCP/UDP via HAL Ethernet/WiFi |
| **Shell & Utilities** | ❌ N/A | Not applicable to embedded RTOS |

### POSIX Thread (pthread) API Coverage

| Function | EoS Status | Notes |
|----------|:----------:|-------|
| `pthread_create` | ✅ | Maps to `eos_task_create` |
| `pthread_join` | ✅ | Waits for task completion |
| `pthread_exit` | ✅ | Task termination |
| `pthread_self` | ✅ | Returns current task ID |
| `pthread_equal` | ✅ | Task ID comparison |
| `pthread_mutex_init` | ✅ | Maps to `eos_mutex_create` |
| `pthread_mutex_lock` | ✅ | Blocking acquire |
| `pthread_mutex_trylock` | ✅ | Non-blocking acquire |
| `pthread_mutex_unlock` | ✅ | Release |
| `pthread_mutex_destroy` | ✅ | Maps to `eos_mutex_destroy` |
| `pthread_cond_init` | ✅ | Condition variable creation |
| `pthread_cond_wait` | ✅ | Block until signaled |
| `pthread_cond_signal` | ✅ | Wake one waiter |
| `pthread_cond_broadcast` | ✅ | Wake all waiters |
| `pthread_rwlock_*` | ✅ | Reader-writer lock family |
| `pthread_barrier_*` | ✅ | Synchronization barrier |
| `pthread_key_create` | ✅ | Thread-local storage |
| `sem_init` | ✅ | Maps to `eos_semaphore_create` |
| `sem_wait` | ✅ | Blocking wait |
| `sem_trywait` | ✅ | Non-blocking wait |
| `sem_post` | ✅ | Signal semaphore |

### POSIX Signal API Coverage

| Function | EoS Status | Notes |
|----------|:----------:|-------|
| `signal` | ✅ | Register handler |
| `raise` | ✅ | Send signal to self |
| `kill` | ✅ | Send signal to task |
| `sigaction` | ✅ | Advanced handler registration |
| `sigprocmask` | ✅ | Block/unblock signals |
| `sigsuspend` | ✅ | Wait for signal |
| `sigpending` | ✅ | Query pending signals |

### POSIX I/O API Coverage

| Function | EoS Status | Notes |
|----------|:----------:|-------|
| `open` | ✅ | Open file/device |
| `close` | ✅ | Close descriptor |
| `read` | ✅ | Read data |
| `write` | ✅ | Write data |
| `lseek` | ✅ | Seek position |
| `ioctl` | ✅ | Device control |
| `select` | ⚠️ | Simplified implementation |
| `poll` | ⚠️ | Simplified implementation |
| `mmap` | ⚠️ | Shared memory only |

---

## 3. Linux Standard Base (LSB)

### Standard Overview

| Attribute | Detail |
|-----------|--------|
| **Full Title** | Linux Standard Base |
| **Current Version** | LSB 5.0 |
| **Purpose** | Binary compatibility between Linux distributions |
| **Modules** | Core, Desktop, Languages, Imaging, Trial Use |

### EoS LSB Relevance

EoS is not a Linux distribution and does not target LSB binary compatibility. However, EoS provides a Linux compatibility layer (`eos/src/compat/linux/`) for developers porting Linux applications to EoS embedded platforms.

| LSB Module | EoS Relevance | Implementation |
|------------|:-------------:|----------------|
| **LSB Core** | ⚠️ Partial | Linux IPC compatibility layer |
| **LSB Desktop** | ❌ N/A | No X11/GTK/Qt |
| **LSB Languages** | ❌ N/A | No runtime interpreters |
| **LSB Imaging** | ❌ N/A | No printing subsystem |

### Linux IPC Compatibility

EoS provides Linux-compatible IPC through `eos/src/compat/linux/eos_linux_ipc.c`:

| Linux IPC | EoS Status | Notes |
|-----------|:----------:|-------|
| System V message queues | ✅ | `msgget/msgsnd/msgrcv` |
| System V semaphores | ✅ | `semget/semop` |
| System V shared memory | ✅ | `shmget/shmat/shmdt` |
| POSIX message queues | ✅ | Via POSIX compat layer |
| Pipes | ⚠️ | In-process only |
| Unix domain sockets | ⚠️ | Partial, via `eipc` transport |

---

## 4. EoS Compatibility Layers

### Architecture

```
┌─────────────────────────────────────────────┐
│           Application Code                   │
│  (POSIX / Linux / VxWorks API calls)        │
├─────────┬──────────────┬────────────────────┤
│  POSIX  │    Linux     │     VxWorks        │
│  Compat │    Compat    │     Compat         │
│  Layer  │    Layer     │     Layer          │
├─────────┴──────────────┴────────────────────┤
│              EoS Kernel API                  │
│  eos_task_* │ eos_mutex_* │ eos_msg_queue_* │
├─────────────────────────────────────────────┤
│              EoS HAL Layer                   │
└─────────────────────────────────────────────┘
```

### Source Files

| Compatibility Layer | Source File | Header |
|--------------------| -----------|--------|
| POSIX Threads | `eos/src/compat/posix/eos_posix_threads.c` | `<pthread.h>` (EoS) |
| POSIX Signals | `eos/src/compat/posix/eos_posix_signals.c` | `<signal.h>` (EoS) |
| POSIX I/O | `eos/src/compat/posix/eos_posix_io.c` | `<unistd.h>` (EoS) |
| Linux IPC | `eos/src/compat/linux/eos_linux_ipc.c` | `<sys/ipc.h>` (EoS) |
| VxWorks Tasks | `eos/src/compat/vxworks/eos_vxworks_tasks.c` | `<taskLib.h>` (EoS) |
| VxWorks Semaphores | `eos/src/compat/vxworks/eos_vxworks_sem.c` | `<semLib.h>` (EoS) |

---

## 5. API Mapping

### EoS Kernel → POSIX Mapping

| EoS Kernel API | POSIX Equivalent | Notes |
|---------------|-----------------|-------|
| `eos_task_create` | `pthread_create` | Task = thread abstraction |
| `eos_task_delete` | `pthread_cancel` | Task termination |
| `eos_task_delay` | `nanosleep` | Timed delay |
| `eos_mutex_create` | `pthread_mutex_init` | Binary/recursive mutex |
| `eos_mutex_lock` | `pthread_mutex_lock` | Blocking lock |
| `eos_mutex_unlock` | `pthread_mutex_unlock` | Unlock |
| `eos_semaphore_create` | `sem_init` | Counting semaphore |
| `eos_semaphore_wait` | `sem_wait` | Decrement and block |
| `eos_semaphore_signal` | `sem_post` | Increment and wake |
| `eos_msg_queue_create` | `mq_open` | Message queue |
| `eos_msg_queue_send` | `mq_send` | Enqueue message |
| `eos_msg_queue_receive` | `mq_receive` | Dequeue message |
| `eos_timer_create` | `timer_create` | Software timer |

---

## 6. Compliance Matrix

| Standard | Scope | EoS Status | Notes |
|----------|-------|:----------:|-------|
| IEEE 1003.1 Threads | Pthreads API | ✅ Full | 20+ functions implemented |
| IEEE 1003.1 Sync | Mutex, condvar, rwlock, barrier | ✅ Full | Complete synchronization primitives |
| IEEE 1003.1 Semaphores | Named/unnamed semaphores | ✅ Full | POSIX semaphore API |
| IEEE 1003.1 Signals | Signal handling | ✅ Full | sigaction, sigprocmask |
| IEEE 1003.1 I/O | File operations | ⚠️ Partial | Basic open/read/write/close |
| IEEE 1003.1 IPC | Message queues, shared memory | ✅ Full | POSIX IPC |
| IEEE 1003.1 Clocks | clock_gettime, timers | ✅ Full | Real-time clock support |
| IEEE 1003.1 Process | fork, exec, wait | ❌ N/A | RTOS task model instead |
| IEEE 1003.1 Shell | sh, utilities | ❌ N/A | Not applicable |
| LSB Core | Binary compatibility | ⚠️ Partial | Linux IPC compat only |
| LSB Desktop | GUI libraries | ❌ N/A | Not applicable |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1.0 | 2026-03-31 | Initial POSIX/LSB compliance document |
