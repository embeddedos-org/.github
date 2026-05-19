"""Build branches.csv (Phase A.2) for the production-readiness audit.

For every repo in embeddedos-org, walks every non-default branch, calls
`gh api compare` to get ahead/behind, classifies disposition, and writes
a CSV at /home/spatchava/embeddedos-org/.github-repo/audit-2026-05/branches.csv.

Disposition rules:
- behind only (ahead == 0)                     -> delete-stale
- diverged with dependabot/* prefix            -> close-pr-then-delete
- diverged with chore/production-ready-cicd    -> delete-stale (these all have ahead==0 already)
- diverged otherwise                           -> inspect
- (no other states are observed in the data)
"""
from __future__ import annotations

import csv
import json
import os
import subprocess
from pathlib import Path

OUT_DIR = Path('/home/spatchava/embeddedos-org/.github-repo/audit-2026-05')
OUT_CSV = OUT_DIR / 'branches.csv'
OUT_DIR.mkdir(parents=True, exist_ok=True)


def gh(args: list[str]) -> str:
    return subprocess.check_output(['gh'] + args, text=True).strip()


def gh_json(args: list[str]):
    return json.loads(gh(args))


def classify(branch: str, ahead: int, behind: int) -> tuple[str, str]:
    """Return (disposition, reason)."""
    if ahead == 0 and behind == 0:
        return 'delete-stale', 'identical to default (zero divergence)'
    if ahead == 0 and behind > 0:
        return 'delete-stale', f'every commit already on default (behind {behind})'
    # ahead > 0 territory
    if branch.startswith('dependabot/'):
        return 'close-pr-then-delete', 'dependabot branch superseded by current default'
    if branch == 'chore/production-ready-cicd':
        return 'delete-stale', 'CI hygiene branch fully merged forward'
    if branch.startswith('achievement/'):
        return 'inspect', f'GitHub achievement branch ({ahead} ahead) — likely no real value'
    if branch == 'ci/add-codeowners':
        return 'inspect', f'CODEOWNERS bump ({ahead} ahead) — verify if applied to default already'
    if branch == 'security-hardening':
        return 'inspect', f'security work ({ahead} ahead) — must not be silently dropped'
    if branch.startswith(('feat/', 'feature/', 'fix/', 'refactor/', 'docs/')):
        return 'inspect', f'feature/fix branch ({ahead} ahead, {behind} behind) — review commits'
    return 'inspect', f'unknown branch shape ({ahead} ahead, {behind} behind)'


def main() -> int:
    repos = gh_json(['repo', 'list', 'embeddedos-org', '--limit', '100', '--json', 'name,defaultBranchRef'])
    repo_default: dict[str, str] = {r['name']: r['defaultBranchRef']['name'] for r in repos if r['defaultBranchRef']}

    rows: list[dict[str, str]] = []
    for repo, default in sorted(repo_default.items()):
        try:
            branches = gh_json(['api', f'repos/embeddedos-org/{repo}/branches', '--paginate'])
        except subprocess.CalledProcessError:
            continue
        for b in branches:
            name = b['name']
            if name == default:
                continue
            try:
                cmp = gh_json(['api', f'repos/embeddedos-org/{repo}/compare/{default}...{name}'])
                ahead = cmp.get('ahead_by', 0)
                behind = cmp.get('behind_by', 0)
                status = cmp.get('status', '')
            except subprocess.CalledProcessError:
                ahead, behind, status = -1, -1, 'compare-failed'
            disposition, reason = classify(name, ahead, behind)
            rows.append({
                'repo': repo,
                'default_branch': default,
                'branch': name,
                'ahead': str(ahead),
                'behind': str(behind),
                'status': status,
                'disposition': disposition,
                'reason': reason,
            })
            print(f'  {repo}: {name} ahead={ahead} behind={behind} -> {disposition}')

    fields = ['repo', 'default_branch', 'branch', 'ahead', 'behind', 'status', 'disposition', 'reason']
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    # Summary
    counts: dict[str, int] = {}
    for r in rows:
        counts[r['disposition']] = counts.get(r['disposition'], 0) + 1
    print()
    print(f'Wrote {len(rows)} branch dispositions to {OUT_CSV}')
    for d, c in sorted(counts.items()):
        print(f'  {d}: {c}')

    # Need-renaming-to-master (default==main)
    main_repos = [n for n, d in repo_default.items() if d == 'main']
    print()
    print(f'Repos still on `main` (need rename to master): {len(main_repos)}')
    for r in main_repos:
        print(f'  - {r}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
