#!/usr/bin/env python3
"""Resolve and validate the EoSim tag for the install-eosim composite action.

Fails closed: only tags of the form ``vX.Y.Z`` are accepted, and (with
``--check-remote``) the tag must exist in the upstream repo. EoSim publishes
no wheel for any release, so consumers should prefer ``from-source`` mode;
this module only resolves the tag, it never installs anything.

Used by ``.github/actions/install-eosim/action.yml`` and unit-tested in
``tests/community/test_install_eosim.py``.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys

TAG_RE = re.compile(r"^v\d+\.\d+\.\d+$")
UPSTREAM = "https://github.com/embeddedos-org/EoSim.git"


def normalize_tag(raw: str) -> str:
    """Return the canonical tag form for a user-supplied version string.

    Accepts ``3.0.2`` or ``v3.0.2`` (surrounding whitespace is stripped) and
    returns ``v3.0.2``. Raises :class:`ValueError` for anything else — in
    particular the historic ``0.1.0`` pin is rejected only if it is not a
    real tag (see :func:`tag_exists`); the format gate stays purely
    syntactic so it cannot drift out of sync with the release list.
    """
    tag = raw.strip()
    if not tag.startswith("v"):
        tag = "v" + tag
    if not TAG_RE.match(tag):
        raise ValueError(
            f"refusing tag {raw!r}: must look like vX.Y.Z (e.g. v3.0.2)"
        )
    return tag


def tag_exists(tag: str, upstream: str = UPSTREAM) -> bool:
    """Return True iff ``tag`` exists in the upstream repo (fail closed)."""
    proc = subprocess.run(
        ["git", "ls-remote", "--tags", upstream, f"refs/tags/{tag}"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    return proc.returncode == 0 and bool(proc.stdout.strip())


def resolve(raw: str, check_remote: bool = False) -> str:
    """Normalize ``raw`` and, optionally, verify it exists upstream."""
    tag = normalize_tag(raw)
    if check_remote and not tag_exists(tag):
        raise ValueError(
            f"refusing tag {tag!r}: no such tag in {UPSTREAM} "
            "(EoSim has no v0.1.0 tag and never published a wheel; "
            "use a real tag such as v3.0.2)"
        )
    return tag


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version", help="requested EoSim version, e.g. 3.0.2 or v3.0.2")
    parser.add_argument(
        "--check-remote",
        action="store_true",
        help="verify the tag exists upstream (fail closed)",
    )
    args = parser.parse_args(argv)
    try:
        print(resolve(args.version, check_remote=args.check_remote))
    except ValueError as exc:
        print(f"install-eosim: error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
