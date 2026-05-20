# EoStudio :: security-hardening

## Commits ahead of master
- 53196e8d10 security: add CI/CD workflows, plugin sandboxing, LLM data protection

## Files changed
- added: .github/workflows/codeql.yml (+21 -0)
- added: .github/workflows/nightly.yml (+27 -0)
- added: .github/workflows/release.yml (+21 -0)
- added: .github/workflows/scorecard.yml (+27 -0)
- added: .github/workflows/weekly.yml (+26 -0)
- modified: README.md (+32 -0)
- modified: eostudio/core/ai/agent.py (+11 -2)
- modified: eostudio/core/ai/llm_client.py (+89 -3)
- modified: eostudio/core/ai/smart_chat.py (+8 -2)
- modified: eostudio/plugins/plugin_base.py (+179 -15)

## Recommendation
Open https://github.com/embeddedos-org/EoStudio/compare/master...security-hardening and decide:
merge `gh api -X POST repos/embeddedos-org/EoStudio/merges -f base=master -f head=security-hardening` ; or
delete `gh api -X DELETE repos/embeddedos-org/EoStudio/git/refs/heads/security-hardening`.
