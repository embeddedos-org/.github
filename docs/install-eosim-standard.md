# install-eosim is the org-standard EoSim setup action (2026-10-07)

`install-eosim` is the **org-standard way to install EoSim in CI**. Any
workflow that installs EoSim via a pinned git tag, a pip pin, or an inline
install script should use the shared action instead.

## Why

Inline EoSim install steps fail as a class: a repo clones a hardcoded tag
without validation, the tag does not exist, every "Install EoSim" step 404's
repo-by-repo with no single fix point. The shared action is the single fix
point — one place to pin, one place to validate, one place to roll forward.
The default installs from a validated git tag (`version` input, default
`3.0.2`, checked remotely before cloning; fails closed on malformed or
nonexistent tags) and verifies the install with `eosim list`. EoSim#16
(platform.yml schema work) is the live example of the kind of simulator change
that downstream CI must absorb through one install path, not N inline steps.

## Migration recipe

Replace any inline EoSim install step:

```yaml
# before (unvalidated inline clone — the failure class)
- run: git clone --depth 1 --branch v2.4.1 https://github.com/embeddedos-org/EoSim.git
```

with the shared action (`.github/actions/install-eosim`; see eApps#49 for the
org's adoption template and copy its shape rather than inventing a new one per
repo):

```yaml
- uses: embeddedos-org/.github/.github/actions/install-eosim@master
  with:
    version: "3.0.2"
```

eApps#49 is the reference adoption; copy its shape rather than inventing a new
one per repo.

## Second standard-to-be (review-only today)

`.github#14` and eNI#42 are the same bug class: a `.coveragerc`
`omit '*tests*'` glob never matches under coverage 7, so test files silently
stay in coverage measurement. The fix pattern (explicit
`*/tests/*` in omit, plus a ratchet) is a candidate for a second org standard
once both PRs land. Review-only — do not invent the standard here.
