#!/usr/bin/env bash
# Phase B — small-repo batch (session 1).
# Operates entirely against GitHub API; local clones untouched.
set -uo pipefail   # NOT -e — we want to continue on per-repo errors

ORG=embeddedos-org

rename_main_to_master() {
  local repo=$1
  local cur=$(gh api "repos/${ORG}/${repo}" --jq '.default_branch')
  if [ "$cur" = "master" ]; then
    echo "  [skip] default already 'master'"
    return 0
  fi
  echo "  rename: ${cur} -> master"
  gh api -X POST "repos/${ORG}/${repo}/branches/${cur}/rename" -f new_name=master --silent && \
    echo "    OK" || echo "    FAIL"
}

delete_branch() {
  local repo=$1
  local branch=$2
  echo "  delete: ${branch}"
  gh api -X DELETE "repos/${ORG}/${repo}/git/refs/heads/${branch}" --silent && \
    echo "    OK" || echo "    (already absent / fail)"
}

create_release_branch() {
  local repo=$1
  # Skip if already exists
  if gh api "repos/${ORG}/${repo}/branches/release" --silent 2>/dev/null; then
    echo "  release branch already exists; skipping"
    return 0
  fi
  local sha=$(gh api "repos/${ORG}/${repo}/git/refs/heads/master" --jq '.object.sha')
  echo "  create: release @ ${sha:0:10}"
  gh api -X POST "repos/${ORG}/${repo}/git/refs" -f ref=refs/heads/release -f sha="$sha" --silent && \
    echo "    OK" || echo "    FAIL"
}

list_branches() {
  local repo=$1
  gh api "repos/${ORG}/${repo}/branches" --paginate --jq '.[].name' | sort | tr '\n' ' '
  echo
}

process() {
  local repo=$1
  shift
  echo
  echo "================================================================"
  echo "  $repo"
  echo "================================================================"
  echo "  BEFORE: $(list_branches "$repo")"
  for op in "$@"; do
    case "$op" in
      rename) rename_main_to_master "$repo" ;;
      release) create_release_branch "$repo" ;;
      delete:*) delete_branch "$repo" "${op#delete:}" ;;
      *) echo "  [unknown op: $op]" ;;
    esac
  done
  echo "  AFTER:  $(list_branches "$repo")"
}

# ---- The actual batch ----
# Order: simplest first.

# 1. .github (on main; 1 branch; no extras)
process .github rename release

# 2. eFab (on main; 1 branch; no extras)
process eFab rename release

# 3. www.embeddedos.org (already master; 1 branch; no extras)
process www.embeddedos.org release

# 4. eVera (master; 1 stale)
process eVera delete:chore/production-ready-cicd release

# 5. embeddedos-org (on main; 1 stale)
process embeddedos-org delete:chore/production-ready-cicd rename release

# 6. eosllm (on main; 1 stale)
process eosllm delete:chore/production-ready-cicd rename release

# 7. eOffice (master; 2 stale)
process eOffice delete:chore/production-ready-cicd delete:fix/workspace-structure release

echo
echo "================================================================"
echo "  DONE — session 1 small-repo batch complete"
echo "================================================================"
