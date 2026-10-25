# The llms.txt knowledge-base pair is the org standard (2026-10-19)

Every EmbeddedOS product repo carries a **knowledge-base pair** at its
root — `llms.txt` + `llms-full.txt` — so an AI agent (or a human
skimming like one) can discover what the repo knows without crawling
its tree. This document is the standard: the shape, the sourcing
rule, the drift check, and the adoption census. It is the light layer
of the org knowledge base in the Agent fabric; the deep layer (an
embeddedos-docs MCP server over the website docs) is separate work.

## Why

Agents are now first-class consumers of these repos — the daily
improvement loop, the MCP gateway, external assistants. A repo whose
documentation exists only as a tree of Markdown files forces every
agent to re-derive the map on every visit, and each agent derives a
different one. The pair fixes the map once, in the repo, where the
docs themselves live: `llms.txt` is the index an agent reads first,
`llms-full.txt` is the full text it loads when the index says the
knowledge is here. One convention, every repo, no per-repo invention.

## The shape

Both files live at the **repo root**. No other location is a pair.

`llms.txt`:

1. `# <repo name>` title.
2. A blockquote summary: what the repo is, its status, and its
   headline facts (version, platform, role in the ecosystem) — the
   paragraph an agent quotes when asked "what is this repo".
3. A short prose paragraph placing the repo in the EmbeddedOS
   ecosystem.
4. `## Docs` — one bullet per source document:
   `- [Title](relative/path.md) — one-line description`. Every path
   must exist in the tree at that exact path.
5. `## Machine-readable` — a single bullet linking `llms-full.txt`.

`llms-full.txt`: the concatenation of exactly the documents listed
in `llms.txt`, in the listed order, full text, nothing else. No
generated content, no paraphrase, no README recycling to pad the
size — a small repo's pair is honestly small (eDB's is 11,653 B
from 3 docs; that is correct, not a defect).

Model examples: `eBoot` (index shape) and `eosllm` (summary shape)
in their repos.

## The sourcing rule

- **Only documents that exist in the tree**, at the paths the index
  names. The pre-landing check is mechanical: every listed path is
  read back from the live tree before the pair is committed.
- **Vendored content is excluded.** ebuild's pair covers ebuild's
  own 8 docs and deliberately omits its vendored `core/` mirrors:
  duplicating upstream content into `llms-full.txt` inflates the
  pair, misattributes authorship, and goes stale against the vendor
  tree.
- **No invented facts.** If a fact has no source in the repo (a
  specification value, a limit, a date), the pair does not state
  it. Where a topic is known-open, the pair may index the document
  that records it as open — it may not resolve it. (eNI's pair
  indexes the #38 audit set including the open F3-3 note, and
  states no frequency value, because none exists to source.)

## The drift check (the guard)

A pair drifts when a listed doc changes and `llms-full.txt` is not
regenerated, or when the index names a path that no longer exists.
The guard is procedural today and is specified here so it is
implemented once, org-wide, not six times per repo:

1. **Recorded provenance.** Every commit that lands or regenerates
   a pair names its source documents and the pair's total byte size
   in the commit body. The census below is rebuilt from live trees,
   never from memory.
2. **Regeneration rule.** Any change to a document listed in a
   repo's `llms.txt` regenerates that repo's `llms-full.txt` in the
   same commit. A docs PR that changes a listed doc without
   touching `llms-full.txt` is incomplete.
3. **Census check.** The org census (this document's table) is
   re-measured against live trees whenever it is quoted — the
   2026-10-18 recount found a standup quoting 17/26 against a true
   15/26, which is why no census number is ever carried forward
   unverified.

A reusable CI workflow implementing (2) mechanically — comparing
each listed doc against its section of `llms-full.txt` — is the
intended end state and belongs in this repo next to
`reusable-server-json.yml`; until it exists, the daily loop's
per-commit CI verification is the enforcement.

**Implemented (2026-10-20):** `scripts/check-llms-drift.py` in
this repo performs that mechanical comparison today, locally:
given a repo directory it verifies that `llms.txt` references
`llms-full.txt`, that every path linked from `llms.txt` exists,
that `llms-full.txt`'s "Sources, in order:" list matches its
section headers in order, and that every section body is
byte-identical to its source doc — printing the first divergent
offset when one is not. Exit 0 means in sync. The reusable
workflow above remains the end state; the script is the check
it will run.

## Adoption census (verified 2026-10-21, live trees; eSec, eNet and embeddedos-stack rows refreshed 2026-10-23; embeddedos-stack row refreshed 2026-10-24; eos and eNet rows refreshed 2026-10-24, evening additional run)

21 of 26 repos carry the pair. Sizes are `llms-full.txt` bytes as
measured from the live trees on the census date.

| Repo | llms-full.txt (B) | Notes |
| --- | ---: | --- |
| eos | 85,414 | incl. the #148 indirection design + size inventory; + MQTT client design (eos#199) |
| eBoot | 106,557 | |
| ebuild | 59,557 | own 8 docs only; vendored `core/` excluded |
| eAI | 30,338 | |
| eosllm | 98,437 | also carries `server.json` |
| eNI | 48,330 | incl. the #38 audit set; F3-3 stated as open, no value |
| eIPC | 79,637 | |
| EoSim | 67,824 | also carries `server.json` + skills |
| EoStudio | 66,670 | |
| eSec | 39,520 | |
| eNet | 43,978 | incl. the home-systems plan (eNet#7) |
| eFlow | 8,055 | also carries `server.json` + a skill |
| eDB | 11,653 | 3 docs — the repo's real docs surface |
| eApps | 32,652 | |
| eBrowser | 18,246 | |
| eOffice | 27,999 | |
| eCAD-Hardware-Products | 327,085 | largest pair (board catalogue docs) |
| eFirmware | 18,562 | |
| eos-aero | 14,548 | |
| embeddedos-stack | 53,242 | private; pair carries no credential material |
| (second private repo) | 44,268 | private; counted but not named — see the note below |

Note on the unnamed row: the 21st pair lives in the org's second
private repo (the on-device agent). Its name is a banned token in
this repository — the canon validator
(`scripts/check-product-canon.py`) forbids the dropped product's
name in `.github` documents — so the census counts it without
naming it. The daily loop's own census records name it; this
standard respects the gate as written rather than exempting
itself from it.

### The five gaps, with reasons

| Repo | Why there is no pair |
| --- | --- |
| eos-health | Deliberate: the repo's structure is undecided (issues #2/#3 — restore / repoint / merge the split firmware trees). A pair indexing a tree that may be restructured is rework on landing; the pair follows the decision. |
| `www.embeddedos.org` | Deliberate: the site's docs need their own selection pass (its content model is pages/routes, not a docs tree). A future rotation item, not a straggler. |
| embeddedos-org.github.io | Parked per Aswin (2026-10-02) — the legacy site is untouched until he says otherwise. |
| .github | Meta repo — **no pair, by this standard's decision.** Its documents are org standards consumed by the other repos (this file included); agent discovery for them is the README table, and a self-indexing pair would duplicate it. Revisit if the standards set grows past what the README table can carry. |
| embeddedos-org | Meta repo — **no pair, by the same decision.** The repo is a single profile README; there is no docs surface to index. |

## Adopt it

For a repo without a pair (a new repo, or one whose gap reason has
closed): assemble the pair from the repo's existing docs only,
verify every listed path against the live tree, land both files in
one commit whose body names the source documents and total bytes,
and update the census table here in the same change or the next
`.github` change. New repos are seeded with the pair once they have
docs worth indexing — not before (an empty pair is worse than
none).
