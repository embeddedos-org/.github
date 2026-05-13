# 🔒 Security Policy

[![Security](https://img.shields.io/badge/security-disclosure-red?style=for-the-badge)](mailto:security@embeddedos.org)
[![Response SLA](https://img.shields.io/badge/ack-24h-orange?style=for-the-badge)](#response-sla)

This file lives in the org-wide `embeddedos-org/.github` repository and is the
**default SECURITY.md** that GitHub surfaces for every repository in the
[EmbeddedOS](https://github.com/embeddedos-org) organisation that does not
ship its own.

## Reporting a Vulnerability

**Email:** <security@embeddedos.org>

> **Do NOT** open public GitHub issues for security vulnerabilities.

Where possible, prefer GitHub's
[private security advisories](https://docs.github.com/code-security/security-advisories)
on the affected repo — that lets us coordinate the fix and credit you publicly
on disclosure.

### What to include

- Affected repository, component(s), and version(s) / commit hash
- Step-by-step reproduction instructions
- Proof-of-concept code, network capture, or crash dump (if available)
- Impact assessment (confidentiality / integrity / availability)
- Whether you intend to publish; preferred coordinated-disclosure date

## Supported Versions

Each product repository declares its own supported-version matrix in its own
`SECURITY.md`. As a general default for the EmbeddedOS organisation:

| Version | Supported |
|---------|-----------|
| Latest released `vX.Y.Z` | ✅ Yes |
| Previous minor `vX.(Y-1).Z` | 🟡 Best effort, security patches only |
| Older | ❌ No |

## Response SLA

| Phase        | Timeline  |
|--------------|-----------|
| Acknowledge  | 24 hours  |
| Triage       | 72 hours  |
| Fix released | 90 days   |

For 0-days under active exploitation, we will accelerate this timeline and
may issue an emergency advisory ahead of the full fix.

## Safe Harbor

We consider security research conducted in good faith to be authorised and
will not pursue legal action against researchers who follow responsible
disclosure practices outlined in this document.

## Per-repository policies

Where a repo ships its own `SECURITY.md`, that file takes precedence over this
default for the specific component it covers. Notable per-repo policies:

- [embeddedos-org.github.io/SECURITY.md](https://github.com/embeddedos-org/embeddedos-org.github.io/blob/master/SECURITY.md)
- [eFab/SECURITY.md](https://github.com/embeddedos-org/eFab/blob/main/SECURITY.md)

## Hall of Fame

We credit researchers in the affected repository's release notes (with their
permission). Reach out via the email above if you would prefer a different
form of acknowledgement.
