# eIPC :: fix/security-and-lint-fixes

## Commits ahead of master
- ac20e525f0 fix(security): address path traversal, buffer overflow and logic vulnerabilities
- 5b56a9300c chore(ci): fix linting and cross-platform path issues in tests
- 550d062caf fix(security): address vulnerabilities + fix all errcheck lint errors

## Files changed
- modified: cmd/eipc-cli/main.go (+10 -8)
- modified: cmd/eipc-client/main.go (+26 -24)
- modified: cmd/eipc-server/main.go (+161 -83)
- modified: config/config.go (+2 -0)
- modified: config/config_test.go (+3 -2)
- modified: core/benchmark_test.go (+1 -1)
- modified: core/endpoint.go (+21 -13)
- modified: core/lifecycle.go (+4 -1)
- modified: core/router_test.go (+2 -2)
- modified: core/types.go (+3 -0)
- modified: protocol/benchmark_test.go (+2 -2)
- modified: protocol/frame.go (+8 -0)
- modified: protocol/fuzz_test.go (+1 -1)
- modified: sdk/c/src/eipc_client.c (+13 -0)
- modified: security/auth/identity.go (+2 -5)
- modified: security/encryption/aes_test.go (+46 -15)
- modified: security/keyring/keyring.go (+2 -4)
- modified: security/keyring/keyring_test.go (+46 -15)
- modified: services/audit/audit.go (+3 -1)
- modified: services/audit/audit_test.go (+20 -9)
- modified: services/broker/broker.go (+1 -1)
- modified: services/broker/broker_test.go (+3 -3)
- modified: services/policy/policy.go (+4 -4)
- modified: services/registry/registry_test.go (+3 -3)
- modified: tests/integration_test.go (+7 -7)
- modified: tests/stress_test.go (+1 -1)
- modified: transport/shm/shm.go (+9 -7)
- modified: transport/shm/shm_test.go (+2 -2)
- modified: transport/tcp/tcp.go (+4 -4)
- modified: transport/tcp/tls_config.go (+5 -0)

## Recommendation
Open https://github.com/embeddedos-org/eIPC/compare/master...fix/security-and-lint-fixes and decide:
merge `gh api -X POST repos/embeddedos-org/eIPC/merges -f base=master -f head=fix/security-and-lint-fixes` ; or
delete `gh api -X DELETE repos/embeddedos-org/eIPC/git/refs/heads/fix/security-and-lint-fixes`.
