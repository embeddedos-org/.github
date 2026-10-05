"""Unit tests for the install-eosim composite action's tag resolver.

Covers ``.github/actions/install-eosim/resolve_eosim_tag.py`` — the
fail-closed tag normalization/validation that replaces the dead
``EOSIM_VERSION: "0.1.0"`` pin family. No network access: remote checks are
tested via monkeypatched ``tag_exists``.
"""
import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE = (
    REPO_ROOT / ".github" / "actions" / "install-eosim" / "resolve_eosim_tag.py"
)


def _load():
    spec = importlib.util.spec_from_file_location("resolve_eosim_tag", MODULE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["resolve_eosim_tag"] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def mod():
    if not MODULE.exists():
        pytest.skip(f"{MODULE} not found")
    return _load()


def test_normalize_accepts_bare_and_v_prefixed(mod):
    assert mod.normalize_tag("3.0.2") == "v3.0.2"
    assert mod.normalize_tag("v3.0.2") == "v3.0.2"
    assert mod.normalize_tag("  v1.5.0\n") == "v1.5.0"


def test_normalize_rejects_non_tag_shapes(mod):
    for bad in [
        "", "v3", "3.0", "v3.0.2.1", "latest", "v3.0.2-rc1", "vX.Y.Z",
        "../../etc/passwd", "v3.0.2; rm -rf /",
    ]:
        with pytest.raises(ValueError):
            mod.normalize_tag(bad)


def test_resolve_without_remote_check_is_pure(mod):
    assert mod.resolve("3.0.2") == "v3.0.2"


def test_resolve_remote_failure_is_fail_closed(mod, monkeypatch):
    monkeypatch.setattr(mod, "tag_exists", lambda tag, upstream=None: False)
    with pytest.raises(ValueError, match="no such tag"):
        mod.resolve("0.1.0", check_remote=True)


def test_resolve_remote_success(mod, monkeypatch):
    monkeypatch.setattr(mod, "tag_exists", lambda tag, upstream=None: True)
    assert mod.resolve("v3.0.2", check_remote=True) == "v3.0.2"


def test_cli_rejects_bad_tag(mod, capsys):
    assert mod.main(["not-a-tag"]) == 1
    assert "must look like vX.Y.Z" in capsys.readouterr().err


def test_cli_prints_resolved_tag(mod, capsys, monkeypatch):
    monkeypatch.setattr(mod, "tag_exists", lambda tag, upstream=None: True)
    assert mod.main(["3.0.2", "--check-remote"]) == 0
    assert capsys.readouterr().out.strip() == "v3.0.2"
