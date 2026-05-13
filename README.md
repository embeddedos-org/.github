# embeddedos-org/.github

Org-wide configuration repo for the [EmbeddedOS](https://github.com/embeddedos-org)
GitHub organisation. GitHub renders [`profile/README.md`](profile/README.md) at
<https://github.com/embeddedos-org> as the org's company-profile page, and
surfaces the rest of this repo as the **default community-health files** for
every other repository in the org that does not ship its own.

This repo deliberately contains **no product source code**.

## What lives here

| Path | What it is | Why it lives here |
|---|---|---|
| `profile/README.md` | Org company-profile page rendered at <https://github.com/embeddedos-org>. | Only file GitHub treats as the org front door. Keep it short. |
| `CODE_OF_CONDUCT.md` | Contributor Covenant 2.1. | GitHub surfaces it as the default CoC for every product repo. |
| `CONTRIBUTING.md` | Org-wide contribution guide (short, points to per-repo guides). | GitHub surfaces it as the default CONTRIBUTING for every product repo. |
| `SECURITY.md` | Org-wide vulnerability disclosure policy. | GitHub surfaces it as the default SECURITY for every product repo. |
| `.github/ISSUE_TEMPLATE/config.yml` | Routes new issues to the correct downstream product repo. | Default issue-template config across the org. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Default PR template. | Used by any product repo without its own. |
| `.github/workflows/check-canon.yml` | Enforces the canonical 13-product / 14-book roster on this repo. | Mirrors the same workflow in every other org repo. |
| `.github/workflows/health-check.yml` | Weekly link-check of the live site + the org page. | Catches link rot. |
| `.github/workflows/lint-readme.yml` | markdownlint + lychee on every push touching `*.md`. | Keeps the profile and prose tidy. |
| `scripts/check-product-canon.py` | Canon validator. | Lock the 13 / 14 numbers; same script as the other repos for consistency. |
| `LICENSE` | MIT. | Org default. |

## Editing the profile

The profile must stay **short** — it is the front door, not a manual. Anything
that needs more than ~5 minutes to read belongs on the
[website](https://embeddedos-org.github.io) and should be linked from the
profile, not embedded in it.

## Contributing

Open a PR against `profile/README.md` for copy / link / badge changes, or
against `CODE_OF_CONDUCT.md` / `CONTRIBUTING.md` / `SECURITY.md` for
org-wide policy changes. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the
short rules.

Major restructures: please open an issue first.
