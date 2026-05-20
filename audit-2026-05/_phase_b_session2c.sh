#!/usr/bin/env bash
# Resolve the remaining inspect branches:
#   - DELETE the 3 superseded/out-of-scope/already-done branches
#   - Attempt local-clone-based merge for the 4 real security branches
#     with a smart conflict strategy:
#       - .github/workflows/**.yml      -> take MASTER (newer org-uniform version)
#       - all other paths               -> take THEIRS (the branch's security fix)
#     Then push merged master + delete branch.
set -uo pipefail

ORG=embeddedos-org
AUDIT=/home/spatchava/embeddedos-org/.github-repo/audit-2026-05
WORK=/home/spatchava/embeddedos-org/.audit-work
mkdir -p "$WORK"

LOG="${AUDIT}/session2c-actions.log"
: > "$LOG"

log() { echo "$@" | tee -a "$LOG"; }

# ---------------------------------------------------------------------
# Auto-delete (verified or judgement-based)
# ---------------------------------------------------------------------

del() {
  local repo=$1 branch=$2 reason=$3
  log "[DELETE ] ${repo} :: ${branch}"
  log "          reason: ${reason}"
  gh api -X DELETE "repos/${ORG}/${repo}/git/refs/heads/${branch}" --silent 2>/dev/null \
    && log "          deleted" || log "          delete failed"
}

del eApps "refactor/extract-standalone-products" "Superseded — already done via eFab + canonical 13-repo split"
del eNI "feature/blockchain-module" "Out-of-scope for the BCI/Neural-Interface repo — 22 files of Solidity + crypto C code; revive in a dedicated repo if pursued"
del eApps "fix/remove-duplicate-eostudio-hardware-module" "Intent already satisfied on master (the duplicate hardware.py is gone there); branch is the source of the merge conflict, not a fix"

# ---------------------------------------------------------------------
# Smart-merge the 4 security branches via local clone
# ---------------------------------------------------------------------

smart_merge() {
  local repo=$1 branch=$2
  log
  log "[MERGE  ] ${repo} :: ${branch}"

  local dir="${WORK}/${repo}"
  rm -rf "$dir"
  git clone --quiet --no-tags --depth 50 \
    --no-single-branch \
    "git@github.com:${ORG}/${repo}.git" "$dir" 2>&1 | tee -a "$LOG"
  cd "$dir" || return 1

  git config user.name "Srikanth Patchava"
  git config user.email "Srikanth.Patchava@brooksautomation.com"
  git fetch origin "${branch}":"refs/heads/_audit_${branch//\//_}" 2>&1 | tee -a "$LOG"

  git checkout master 2>&1 | tee -a "$LOG" >/dev/null

  # Attempt 3-way merge with default strategy first
  if git merge --no-edit --no-ff "_audit_${branch//\//_}" 2>&1 | tee -a "$LOG"; then
    log "          clean merge"
  else
    log "          conflicts detected; applying smart-resolve rules"
    # For every conflicting file:
    #   if path starts with .github/workflows/ -> take master (--ours)
    #   else -> take theirs (the security branch)
    local conflicted
    conflicted=$(git diff --name-only --diff-filter=U)
    for f in $conflicted; do
      if [[ "$f" == .github/workflows/* ]]; then
        log "            ours (master): $f"
        git checkout --ours -- "$f"
      else
        log "            theirs (security branch): $f"
        git checkout --theirs -- "$f"
      fi
      git add -- "$f"
    done
    if ! git diff --cached --quiet; then
      git commit --no-edit -m "merge(audit-2026-05): ${branch} -> master; .github/workflows kept from master, other paths from ${branch}" 2>&1 | tee -a "$LOG"
    fi
  fi

  # Push merged master
  if git push origin master 2>&1 | tee -a "$LOG"; then
    log "          push OK"
    gh api -X DELETE "repos/${ORG}/${repo}/git/refs/heads/${branch}" --silent 2>/dev/null \
      && log "          branch deleted" || log "          branch delete failed (likely already gone)"
  else
    log "          push FAILED — leaving branch alive"
  fi
}

smart_merge eIPC      "fix/security-and-lint-fixes"
smart_merge EoSim     "security-hardening"
smart_merge EoStudio  "security-hardening"
smart_merge eNI       "security-hardening"

log
log "=== done ==="
