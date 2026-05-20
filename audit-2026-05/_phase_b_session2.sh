#!/usr/bin/env bash
# Session-2 driver. Drives Phase B on the remaining 12 repos.
# Reads disposition from branches.csv:
#   delete-stale         -> DELETE branch (no merge)
#   close-pr-then-delete -> CLOSE PR (if any) with comment, then DELETE branch
#   inspect              -> LEAVE ALONE (surface for user review)
#
# After all repos processed, creates release branch where missing.
set -uo pipefail

ORG=embeddedos-org
CSV=/home/spatchava/embeddedos-org/.github-repo/audit-2026-05/branches.csv

# Skip the 8 already done in session 1
SKIP=("eBrowser" ".github" "eFab" "www.embeddedos.org" "eVera" "embeddedos-org" "eosllm" "eOffice")
skip_me() {
  local r=$1
  for s in "${SKIP[@]}"; do
    [ "$r" = "$s" ] && return 0
  done
  return 1
}

# Find the PR number (if any) for a given head branch on a repo.
find_pr() {
  local repo=$1 branch=$2
  gh pr list --repo "${ORG}/${repo}" --state open --head "$branch" --json number --jq '.[0].number // empty' 2>/dev/null
}

close_pr() {
  local repo=$1 number=$2 reason=$3
  gh pr close "$number" --repo "${ORG}/${repo}" --comment "Closing as part of the 2026-05 branch-hygiene audit. Reason: ${reason}. Master is the line; release tracks the latest vX.Y.Z tag. If this PR is still relevant, please reopen with a rebase against current master." --delete-branch=false >/dev/null 2>&1
}

delete_branch() {
  local repo=$1 branch=$2
  gh api -X DELETE "repos/${ORG}/${repo}/git/refs/heads/${branch}" --silent 2>/dev/null
}

create_release() {
  local repo=$1
  # Check if release exists
  if gh api "repos/${ORG}/${repo}/branches/release" --silent 2>/dev/null; then
    return 0  # already exists
  fi
  local sha
  sha=$(gh api "repos/${ORG}/${repo}/git/refs/heads/master" --jq '.object.sha' 2>/dev/null)
  if [ -z "$sha" ]; then
    return 1
  fi
  gh api -X POST "repos/${ORG}/${repo}/git/refs" -f ref=refs/heads/release -f sha="$sha" --silent
}

# Walk CSV. Skip header. Skip session-1 repos.
declare -A REPO_TOUCHED
declare -i n_delete=0 n_closed=0 n_inspect=0 n_skip=0

while IFS=, read -r repo default branch ahead behind status disposition reason; do
  if [ "$repo" = "repo" ]; then continue; fi      # header
  if skip_me "$repo"; then
    n_skip=$((n_skip+1))
    continue
  fi
  REPO_TOUCHED[$repo]=1

  case "$disposition" in
    delete-stale)
      printf '  [del] %-30s %s\n' "$repo" "$branch"
      delete_branch "$repo" "$branch" && n_delete=$((n_delete+1))
      ;;
    close-pr-then-delete)
      pr=$(find_pr "$repo" "$branch")
      if [ -n "$pr" ]; then
        printf '  [pr-close] %-30s #%-4s %s\n' "$repo" "$pr" "$branch"
        close_pr "$repo" "$pr" "branch superseded by current master; auto-update will be reopened by Dependabot if still needed"
        n_closed=$((n_closed+1))
      fi
      printf '  [del] %-30s %s (post-PR-close)\n' "$repo" "$branch"
      delete_branch "$repo" "$branch" && n_delete=$((n_delete+1))
      ;;
    inspect)
      printf '  [SKIP-inspect] %-30s %s  (%s)\n' "$repo" "$branch" "$reason"
      n_inspect=$((n_inspect+1))
      ;;
    *)
      printf '  [UNKNOWN] %-30s %s -> %s\n' "$repo" "$branch" "$disposition"
      ;;
  esac
done < "$CSV"

echo
echo "=== creating release branch on touched repos ==="
for r in "${!REPO_TOUCHED[@]}"; do
  if create_release "$r"; then
    echo "  release OK: $r"
  else
    echo "  release already present: $r"
  fi
done

echo
echo "=== counts ==="
echo "  deletes:        $n_delete"
echo "  PRs closed:     $n_closed"
echo "  left inspect:   $n_inspect"
echo "  rows skipped:   $n_skip (session-1 repos already done)"
