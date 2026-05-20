# eNI :: feature/blockchain-module

## Commits ahead of master
- a6ef667315 Add blockchain security module for neural data

## Files changed
- modified: CMakeLists.txt (+6 -0)
- added: blockchain/CMakeLists.txt (+50 -0)
- added: blockchain/contracts/ConsentManager.sol (+250 -0)
- added: blockchain/contracts/DeviceRegistry.sol (+246 -0)
- added: blockchain/contracts/NeuralDataRegistry.sol (+194 -0)
- added: blockchain/include/eni_bc/blockchain.h (+49 -0)
- added: blockchain/include/eni_bc/client.h (+94 -0)
- added: blockchain/include/eni_bc/consent.h (+105 -0)
- added: blockchain/include/eni_bc/crypto.h (+87 -0)
- added: blockchain/include/eni_bc/device.h (+105 -0)
- added: blockchain/include/eni_bc/provenance.h (+88 -0)
- added: blockchain/include/eni_bc/sharing.h (+144 -0)
- added: blockchain/include/eni_bc/types.h (+129 -0)
- added: blockchain/src/blockchain.c (+53 -0)
- added: blockchain/src/client.c (+179 -0)
- added: blockchain/src/consent.c (+194 -0)
- added: blockchain/src/crypto.c (+273 -0)
- added: blockchain/src/device.c (+213 -0)
- added: blockchain/src/provenance.c (+175 -0)
- added: blockchain/src/sharing.c (+261 -0)
- added: blockchain/src/types.c (+50 -0)

## Recommendation
Open https://github.com/embeddedos-org/eNI/compare/master...feature/blockchain-module and decide:
merge `gh api -X POST repos/embeddedos-org/eNI/merges -f base=master -f head=feature/blockchain-module` ; or
delete `gh api -X DELETE repos/embeddedos-org/eNI/git/refs/heads/feature/blockchain-module`.
