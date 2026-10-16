# reusable-server-json is the org-standard server.json validation (2026-10-16)

`reusable-server-json.yml` is the **org-standard way to validate an MCP
`server.json`** before publishing. Any repository that ships a
`server.json` (MCP Registry / Server Card metadata) should call the
shared reusable workflow instead of hand-rolling a validator.

## Why

Registry metadata drifts from the package it describes: a repo bumps
its version, forgets `server.json`, and the registry now advertises a
stale server. Per-repo validators fail as a class — the same check
copied N times, fixed in none. The reusable workflow is the single
fix point: one place that defines what a valid `server.json` is for
this org.

## What it checks

Calling `.github/workflows/reusable-server-json.yml` validates:

1. The file at `server_json_path` (default `server.json`) parses as
   JSON.
2. The required fields — `name`, `description`, `version`,
   `repository` — are present and non-empty. Every failure names the
   offending field.
3. **Only when `expected_version` is given:** the `version` field
   matches it exactly. `expected_version` is optional (default `""`)
   — omit it to validate structure only. (It was previously required
   with no usable default, so a copied caller that omitted it failed;
   that blocker was removed 2026-10-15.)

## Adopt it: copy-paste caller

```yaml
jobs:
  server-json:
    uses: embeddedos-org/.github/.github/workflows/reusable-server-json.yml@master
    with:
      server_json_path: server.json
      expected_version: "1.2.0"  # optional; omit for structure-only
```

Pin `expected_version` to your package version wherever the package
has one — that is the drift check doing its job. Omit it only for a
repo whose `server.json` version is deliberately independent.

## Worked examples (the 2026-10-14 adopters)

| Repo | Caller | `expected_version` |
|---|---|---|
| eosllm | `.github/workflows/server-json.yml` | `0.1.0` |
| EoSim | `.github/workflows/server-json.yml` | `3.0.2` |
| eFlow | `.github/workflows/server-json.yml` | `0.1.0` |

Copy one of these callers' shape rather than inventing a new one per
repo.

## Publishing is a separate, manual step

This workflow validates; it does not publish. Publishing to the MCP
Registry with `mcp-publisher` remains a deliberate manual step by a
maintainer — the org does not automate registry publishes, and no
caller should grow a publish step out of this validation workflow.
