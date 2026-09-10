# Repository governance registry

`repositories.json` is the authoritative inventory for EmbeddedOS community-surface rollout. It was reconciled from the read-only organization audit completed at `2026-09-09T02:06:27Z`, which matched 26 local repositories to 26 GitHub repositories with no duplicates or omissions.

The registry deliberately leaves `project_v2` as `null` until a token with `read:project` can inventory links. A writer must not guess Project identities. Update a value only from a recorded GitHub ProjectV2 ID and URL.

The trusted automation allowlist is exact and case-sensitive. `dependabot[bot]` is the sole current exemption. Names, suffixes, labels, branch prefixes, and pull-request text never grant an exemption.

Validate the registry and templates with:

```bash
python3 -m unittest discover -s tests/community -v
```
