# 🤝 Contributing to EmbeddedOS

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](https://github.com/embeddedos-org)
[![Conventional Commits](https://img.shields.io/badge/Commits-Conventional-orange?style=for-the-badge)](https://www.conventionalcommits.org/)
[![Code of Conduct](https://img.shields.io/badge/Contributor_Covenant-2.1-purple?style=for-the-badge)](CODE_OF_CONDUCT.md)

This file lives in the org-wide `embeddedos-org/.github` repo and is the
**default CONTRIBUTING.md** that GitHub surfaces for every product repository
in the [EmbeddedOS](https://github.com/embeddedos-org) organisation.

It is intentionally short. **Detailed coding standards, branching strategy,
review process, and per-component conventions live inside each product
repository's own `CONTRIBUTING.md`** — open the contribution guide of the
specific repo you are changing.

## Where to contribute

EmbeddedOS is a federation of **13 small, independently-versioned product
repositories** plus a handful of meta-repos. Most code contributions belong in
a downstream product repo, not here.

| You want to … | Open the PR / issue here |
|---------------|--------------------------|
| Fix a bug in the OS kernel | [`embeddedos-org/eos`](https://github.com/embeddedos-org/eos) |
| Improve / add a doc page or book | [`embeddedos-org/embeddedos-org.github.io`](https://github.com/embeddedos-org/embeddedos-org.github.io) |
| Add an app to the marketplace | [`embeddedos-org/eApps`](https://github.com/embeddedos-org/eApps) |
| Add or change a stack profile / manifest | [`embeddedos-org/eFab`](https://github.com/embeddedos-org/eFab) |
| Update org-wide policy, templates, CoC, or this file | this repo (`embeddedos-org/.github`) |

For a full list of product repos see the org profile at
<https://github.com/embeddedos-org> or the developer portal at
<https://embeddedos-org.github.io>.

## Org-wide expectations

These apply to **every** repo in the organisation:

- **Code of Conduct** — [Contributor Covenant 2.1](CODE_OF_CONDUCT.md).
- **Security** — disclose privately via [`SECURITY.md`](SECURITY.md), never
  open a public issue for a vulnerability.
- **License** — MIT unless a repo declares otherwise.
- **Commit messages** — [Conventional Commits](https://www.conventionalcommits.org/)
  (`feat(scope):`, `fix(scope):`, `docs(scope):`, `chore(scope):`, etc.).
- **Canonical product roster** — **13 product repos / 14 reference books.**
  The `scripts/check-product-canon.py` validator runs in CI to lock that
  count; bumping it requires a coordinated change across the canon-script
  copies in this repo, [eFab](https://github.com/embeddedos-org/eFab), and
  [embeddedos-org.github.io](https://github.com/embeddedos-org/embeddedos-org.github.io).

## Per-repo contribution guides

Each downstream product ships its own `CONTRIBUTING.md` covering coding
standards, build/test conventions, review process, CLA (where applicable),
security disclosure policy, and signing requirements. Read the per-repo
guide before opening the PR — this org-wide file does **not** override it.

## Quick rules for *this* (`.github`) repo

- Run `npx --yes markdownlint-cli '**/*.md'` before pushing.
- Keep links live — `npx --yes lychee --offline '**/*.md'` should pass.
- Keep [`profile/README.md`](profile/README.md) **short** — it is the org
  front door, not a manual. Anything that grows past one screen of text
  belongs on the [website](https://embeddedos-org.github.io) instead and
  should be linked from the profile.
- Use [Conventional Commits](https://www.conventionalcommits.org/).
- Be kind: every contributor is bound by our [Code of Conduct](CODE_OF_CONDUCT.md).
