#!/usr/bin/env python3
"""Check an EmbeddedOS repo's llms.txt / llms-full.txt pair for drift.

Implements the drift check specified in
docs/knowledge-base-standard.md. The pair is the org-standard
light knowledge-base layer: llms.txt indexes the repo's docs and
llms-full.txt concatenates them, in order, under
``# === <path> ===`` section headers.

For a target repo directory this script verifies, in order:

1. llms.txt references llms-full.txt (the pair is linked).
2. Every relative document path linked from llms.txt exists in
   the tree (no dangling index entries).
3. llms-full.txt's "Sources, in order:" list matches its
   ``# === ... ===`` sections, in the same order.
4. Every section body is byte-identical to its source document
   (sections are separated by one blank line; the final section
   ends the file). A listed doc that changed without a
   regeneration fails here, with the first divergent offset.

Usage:
    python3 scripts/check-llms-drift.py <repo-dir> [<repo-dir> ...]

Exit status: 0 when every pair is in sync, 1 on the first drift
found (printed to stderr), 2 on a usage error or a missing pair.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SECTION_RE = re.compile(r"^# === (.+) ===$", re.MULTILINE)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SOURCE_ITEM_RE = re.compile(r"^- `([^`]+)`$", re.MULTILINE)


class DriftError(Exception):
    """The pair is out of sync; the message names the first divergence."""


class MissingPairError(Exception):
    """The target directory does not carry a complete pair."""


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _check_index_links(repo: Path, llms_txt: str) -> None:
    if "llms-full.txt" not in llms_txt:
        raise DriftError("llms.txt does not reference llms-full.txt")
    for target in LINK_RE.findall(llms_txt):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        if not target or target == "llms.txt":
            continue
        if not (repo / target).exists():
            raise DriftError(f"llms.txt links a path that does not exist: {target}")


def _sources_list(full: str) -> list[str]:
    marker = "Sources, in order:"
    idx = full.find(marker)
    if idx < 0:
        raise DriftError("llms-full.txt has no 'Sources, in order:' list")
    tail = full[idx + len(marker) :]
    end = tail.find("# ===")
    block = tail if end < 0 else tail[:end]
    return SOURCE_ITEM_RE.findall(block)


def _sections(full: str) -> list[tuple[str, str]]:
    matches = list(SECTION_RE.finditer(full))
    sections = []
    for i, m in enumerate(matches):
        start = m.end()
        if full[start : start + 2] == "\n\n":
            start += 2
        elif full[start : start + 1] == "\n":
            start += 1
        end = matches[i + 1].start() if i + 1 < len(matches) else len(full)
        sections.append((m.group(1), full[start:end]))
    return sections


def check_pair(repo: Path) -> int:
    """Return the number of source docs verified for one repo."""
    llms = repo / "llms.txt"
    full_path = repo / "llms-full.txt"
    if not llms.exists() or not full_path.exists():
        raise MissingPairError(f"{repo}: llms.txt / llms-full.txt pair is incomplete")

    llms_txt = _read(llms)
    full = _read(full_path)

    _check_index_links(repo, llms_txt)

    sources = _sources_list(full)
    if not sources:
        raise DriftError("llms-full.txt lists no sources")
    sections = _sections(full)
    if [name for name, _ in sections] != sources:
        raise DriftError(
            "llms-full.txt section order does not match its Sources list: "
            f"sources={sources} sections={[n for n, _ in sections]}"
        )

    for i, (name, body) in enumerate(sections):
        doc_path = repo / name
        if not doc_path.exists():
            raise DriftError(f"llms-full.txt lists a source that does not exist: {name}")
        doc = _read(doc_path)
        expected = doc if i == len(sections) - 1 else doc + "\n"
        if body != expected:
            offset = next(
                (k for k, (a, b) in enumerate(zip(body, expected)) if a != b),
                min(len(body), len(expected)),
            )
            raise DriftError(
                f"{name}: section in llms-full.txt diverges from the source "
                f"doc at offset {offset} (regenerate llms-full.txt; "
                "never hand-edit it)"
            )
    return len(sections)


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__.split("Usage:")[1].strip(), file=sys.stderr)
        return 2
    for arg in argv:
        repo = Path(arg)
        try:
            count = check_pair(repo)
        except MissingPairError as exc:
            print(f"MISSING: {exc}", file=sys.stderr)
            return 2
        except DriftError as exc:
            print(f"DRIFT: {repo}: {exc}", file=sys.stderr)
            return 1
        print(f"OK: {repo}: pair in sync ({count} source docs verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
