# install-eosim (composite action)

Installs EoSim from a pinned, validated git tag — the durable fix for the
`EOSIM_VERSION: "0.1.0"` root-cause family.

## Why this exists

Several org repos pinned `EOSIM_VERSION: "0.1.0"` and either cloned tag
`v0.1.0` or pip-installed a `v0.1.0` wheel. EoSim has **no** `v0.1.0` tag and
**no** release ships a wheel, so every `Install EoSim` step 404'd (eAI's QEMU
Simulation Test / EoSim Sanity / Simulation Test, eApps' sim jobs, eBoot's
Simulation Sanity Test, ebuild#128's desktop sanity jobs).

## Usage

```yaml
- name: Install EoSim
  uses: embeddedos-org/.github/.github/actions/install-eosim@master  # no v1 tag yet; v1.0.0 predates this action
  with:
    version: "3.0.2"        # default; must be a real vX.Y.Z tag (fail closed)
    install-mode: from-source  # default; 'wheel' only if a wheel 200s
```

The action resolves the tag with `resolve_eosim_tag.py` (format gate +
`git ls-remote` existence check — fails closed), clones `--depth 1 --branch`,
pip-installs, then verifies `eosim --version` matches the tag.

## Migration note (for consumer workflows)

Replace both dead patterns:

```yaml
# BEFORE (dead):
- name: Install EoSim
  run: pip install "eosim @ https://github.com/embeddedos-org/EoSim/releases/download/v${{ env.EOSIM_VERSION }}/eosim-${{ env.EOSIM_VERSION }}-py3-none-any.whl"
# or: git clone --depth 1 --branch v${{ env.EOSIM_VERSION }} ...  (with EOSIM_VERSION: "0.1.0")

# AFTER:
- name: Install EoSim
  uses: embeddedos-org/.github/.github/actions/install-eosim@master
```

Then delete the `EOSIM_VERSION` env pin. Rollout to eAI/eBoot/eApps/ebuild
workflows is tracked in the daily standup; the direct tag bumps of 2026-10-05
are the stopgap.

## EoSim engine contracts (for sim steps)

`v3.0.2+` is honest about what it executes:

- **qemu engine**: prints `via qemu` + `PASSED (dry run)`, exit 0 (EoSim#38 —
  the backend never executes qemu without it installed).
- **native engine** without `--firmware`: prints `NO FIRMWARE`, **exit 2**
  (it no longer fakes a pass over zeroed memory).

Sim steps must assert these contracts instead of assuming exit 0; see
eBoot's `eosim-sanity.yml` for the reference pattern. Real firmware execution
is tracked per-repo (e.g. eBoot#147).

## Tests

`tests/community/test_install_eosim.py` covers the resolver (7 tests, no
network). Run: `python3 -m pytest tests/community/test_install_eosim.py`.
