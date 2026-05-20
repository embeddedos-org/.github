#!/usr/bin/env bash
# Final state report after session 2.
set +e
ORG=embeddedos-org
clean=0
remaining=0
echo "=== state after session 2 ==="
printf '%-30s %-9s %s\n' 'repo' 'default' 'branches'
echo '----------------------------------------------------------------------------------------------------'
for r in $(gh repo list ${ORG} --limit 100 --json name -q '.[].name' | sort); do
  default=$(gh api repos/${ORG}/${r} --jq '.default_branch')
  branches=$(gh api repos/${ORG}/${r}/branches --paginate --jq '.[].name' | sort | tr '\n' ' ')
  printf '%-30s %-9s %s\n' "$r" "$default" "$branches"
  # Count clean = exactly "master release "
  if [ "$branches" = "master release " ]; then
    clean=$((clean+1))
  else
    remaining=$((remaining+1))
  fi
done
echo
echo "=== summary ==="
echo "  at {master, release}: $clean / 20"
echo "  still with extra:     $remaining / 20"
