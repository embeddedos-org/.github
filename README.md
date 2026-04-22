# .github

Organization-wide configuration and shared resources for the [EmbeddedOS](https://github.com/embeddedos-org) project.

## Contents

| Path | Description |
|------|-------------|
| `profile/README.md` | Organization profile displayed on [github.com/embeddedos-org](https://github.com/embeddedos-org) |
| `CONTRIBUTING.md` | Contribution guidelines for all EmbeddedOS repositories |
| `CODEOWNERS` | Default code ownership rules |
| `LICENSE` | MIT license for organization-wide files |
| `actions/` | Reusable GitHub Actions (QEMU toolchain setup, rootfs builder) |
| `docs/compliance/` | Standards compliance documentation (ISO, IEC, POSIX, SBOM) |

## Usage

Files in this repository are automatically inherited by all repositories in the `embeddedos-org` organization that do not override them (e.g., `CONTRIBUTING.md`, `CODEOWNERS`).

Reusable actions can be referenced from any repo's workflow:

```yaml
- uses: embeddedos-org/.github/actions/setup-qemu-toolchains@main
```

## Related

- [Developer Portal](https://embeddedos-org.github.io)
- [App Store](https://embeddedos-org.github.io/eApps/)

## License

MIT — see [LICENSE](LICENSE) for details.
