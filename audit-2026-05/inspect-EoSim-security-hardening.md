# EoSim :: security-hardening

## Commits ahead of master
- 753cd07958 security: add CI/CD workflows, harden QEMU/serial/Docker

## Files changed
- added: .github/workflows/codeql.yml (+21 -0)
- added: .github/workflows/nightly.yml (+27 -0)
- added: .github/workflows/release.yml (+21 -0)
- added: .github/workflows/scorecard.yml (+27 -0)
- added: .github/workflows/weekly.yml (+26 -0)
- modified: Dockerfile (+13 -2)
- modified: README.md (+42 -0)
- modified: eosim/engine/qemu/qmp_client.py (+15 -1)
- modified: eosim/integrations/serial_bridge.py (+30 -1)

## Recommendation
Open https://github.com/embeddedos-org/EoSim/compare/master...security-hardening and decide:
merge `gh api -X POST repos/embeddedos-org/EoSim/merges -f base=master -f head=security-hardening` ; or
delete `gh api -X DELETE repos/embeddedos-org/EoSim/git/refs/heads/security-hardening`.
