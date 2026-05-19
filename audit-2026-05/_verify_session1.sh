#!/usr/bin/env bash
# Verify all 8 session-1 repos now have exactly {master, release}.
set +e
for r in eBrowser .github eFab www.embeddedos.org eVera embeddedos-org eosllm eOffice; do
  branches=$(gh api "repos/embeddedos-org/${r}/branches" --paginate --jq '.[].name' | sort | tr '\n' ' ')
  default=$(gh api "repos/embeddedos-org/${r}" --jq '.default_branch')
  echo "${r}: default=${default} branches=[${branches}]"
done
