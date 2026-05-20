#!/usr/bin/env bash
# Final phase-B sweep: act on the 25 inspect branches.
# Each branch is classified into MERGE / DELETE / SURFACE.
# MERGE  -> server-side merge via gh api (squash-style commit) then delete branch.
# DELETE -> just delete the branch (no merit / superseded / out-of-scope / redundant).
# SURFACE -> leave alive, dump diff into audit dir for case-by-case review.
set -uo pipefail

ORG=embeddedos-org
AUDIT=/home/spatchava/embeddedos-org/.github-repo/audit-2026-05
LOG=${AUDIT}/session2b-actions.log
: > "$LOG"

# Format: REPO|BRANCH|ACTION|REASON
ACTIONS="
eos|achievement/pair-contributors|DELETE|GitHub badge auto-branch; no real code value
eos|achievement/pair-extraordinaire|DELETE|GitHub badge auto-branch; no real code value
eos|achievement/yolo-cleanup|DELETE|GitHub badge auto-branch; no real code value
eos|achievement/yolo-gitignore-fix|DELETE|GitHub badge auto-branch; no real code value
eBoot|achievement/update-gitignore|DELETE|GitHub badge auto-branch
eNI|achievement/update-gitignore|DELETE|GitHub badge auto-branch
eAI|ci/add-codeowners|DELETE|CODEOWNERS already on master; bump superseded
eBoot|ci/add-codeowners|DELETE|CODEOWNERS already on master; bump superseded
eIPC|ci/add-codeowners|DELETE|CODEOWNERS already on master; bump superseded
ebuild|ci/add-codeowners|DELETE|CODEOWNERS already on master; bump superseded
eos|ci/add-codeowners|DELETE|CODEOWNERS already on master; bump superseded
eApps|ci/add-auto-assign|DELETE|auto-assign.yml already on master; superseded
eApps|ci/disable-dependabot|DELETE|disabling Dependabot is an anti-pattern for security hygiene
eNI|ci/disable-dependabot|DELETE|disabling Dependabot is an anti-pattern for security hygiene
eNI|docs/add-pr-template|DELETE|org-wide PR template now lives in embeddedos-org/.github
EoSim|security-hardening|MERGE|security work; merge to keep the fix on master
EoStudio|security-hardening|MERGE|security work
eBoot|security-hardening|MERGE|security work
eNI|security-hardening|MERGE|security work
eIPC|fix/security-and-lint-fixes|MERGE|3 commits of security/lint fixes; merge
ebuild|fix/remove-bom-from-eos-ai-test|MERGE|bug fix; merge
eApps|fix/remove-duplicate-eostudio-hardware-module|MERGE|bug fix; merge
eApps|refactor/extract-standalone-products|SURFACE|substantial refactor; review before merging
eNI|feature/blockchain-module|SURFACE|out-of-scope feature for the Neural Interface repo; needs explicit user call
"

attempt_merge() {
  local repo=$1 branch=$2
  # gh api -X POST returns the merge commit on success, or an error body on 409.
  local resp http
  http=$(gh api -X POST "repos/${ORG}/${repo}/merges" \
    -f base=master -f head="${branch}" \
    -f commit_message="merge(audit-2026-05): merge ${branch} into master per branch-hygiene sweep" \
    --silent -i 2>&1 | head -1 | awk '{print $2}' || true)
  echo "$http"
}

delete_branch() {
  local repo=$1 branch=$2
  gh api -X DELETE "repos/${ORG}/${repo}/git/refs/heads/${branch}" --silent 2>/dev/null
}

surface_branch() {
  local repo=$1 branch=$2
  local safe=$(echo "$branch" | tr '/' '_')
  local out="${AUDIT}/inspect-${repo}-${safe}.md"
  {
    echo "# ${repo} :: ${branch}"
    echo
    echo "## Commits ahead of master"
    gh api "repos/${ORG}/${repo}/compare/master...${branch}" \
      --jq '.commits[] | "- \(.sha[0:10]) \(.commit.message | split("\n")[0])"' 2>/dev/null
    echo
    echo "## Files changed"
    gh api "repos/${ORG}/${repo}/compare/master...${branch}" \
      --jq '.files[] | "- \(.status): \(.filename) (+\(.additions) -\(.deletions))"' 2>/dev/null
    echo
    echo "## Recommendation"
    echo "Open https://github.com/${ORG}/${repo}/compare/master...${branch} and decide:"
    echo "merge \`gh api -X POST repos/${ORG}/${repo}/merges -f base=master -f head=${branch}\` ; or"
    echo "delete \`gh api -X DELETE repos/${ORG}/${repo}/git/refs/heads/${branch}\`."
  } > "$out"
  echo "    surfaced to $(basename "$out")"
}

declare -i n_merged=0 n_delete=0 n_conflict=0 n_surface=0

echo "$ACTIONS" | grep -v '^$' | while IFS='|' read -r repo branch action reason; do
  printf '  [%-7s] %-30s %s\n' "$action" "$repo" "$branch" | tee -a "$LOG"
  case "$action" in
    MERGE)
      # API returns "201 Created" on clean merge, "204 No Content" on already-merged, "409 Conflict" on conflict.
      result=$(gh api -X POST "repos/${ORG}/${repo}/merges" \
        -f base=master -f head="${branch}" \
        -f commit_message="merge(audit): pull ${branch} into master (branch-hygiene sweep)" 2>&1)
      status=$?
      if [ "$status" -eq 0 ] || echo "$result" | grep -q '"sha"'; then
        echo "    merge OK; deleting branch" | tee -a "$LOG"
        delete_branch "$repo" "$branch"
        echo "DELETE-AFTER-MERGE-OK" >> "$LOG"
      elif echo "$result" | grep -qi 'merge conflict\|conflict'; then
        echo "    MERGE CONFLICT; leaving branch alive + surfacing" | tee -a "$LOG"
        echo "$result" >> "$LOG"
        surface_branch "$repo" "$branch"
      elif echo "$result" | grep -qi 'nothing to compare\|already exists\|no commits'; then
        echo "    already merged or empty; deleting" | tee -a "$LOG"
        delete_branch "$repo" "$branch"
      else
        echo "    UNEXPECTED: $result" | tee -a "$LOG"
        surface_branch "$repo" "$branch"
      fi
      ;;
    DELETE)
      delete_branch "$repo" "$branch"
      echo "    deleted: $reason" | tee -a "$LOG"
      ;;
    SURFACE)
      echo "    surfacing for review: $reason" | tee -a "$LOG"
      surface_branch "$repo" "$branch"
      ;;
  esac
done

echo
echo "=== written log: $LOG ==="
