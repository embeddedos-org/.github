#!/usr/bin/env bash
# Trial run on eBrowser. ONE branch to delete, then create release.
set -euo pipefail

REPO=embeddedos-org/eBrowser
DEFAULT=master

echo "=== before ==="
gh api "repos/${REPO}/branches" --paginate --jq '.[].name' | sort

echo
echo "=== delete chore/production-ready-cicd ==="
gh api -X DELETE "repos/${REPO}/git/refs/heads/chore/production-ready-cicd"
echo "  deleted"

echo
echo "=== create release branch from ${DEFAULT} HEAD ==="
sha=$(gh api "repos/${REPO}/git/refs/heads/${DEFAULT}" --jq '.object.sha')
echo "  master SHA: $sha"
gh api -X POST "repos/${REPO}/git/refs" -f ref=refs/heads/release -f sha="$sha"
echo "  release created"

echo
echo "=== after ==="
gh api "repos/${REPO}/branches" --paginate --jq '.[].name' | sort
