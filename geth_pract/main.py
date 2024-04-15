from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=contract_address, abi=abi)

print(contract.address)
print(w3.eth.get_balance("0x6CFBC0210F9488A03c661795f87FE2Ee76e94a45"))
print(w3.eth.get_balance("0xdbC2911a5B9AB02F05aE081410b50965EA36263a"))
print(w3.eth.get_balance("0x94c8D41A3fd018Bca35d2B84a1281Cf776aCddAF"))
print(w3.eth.get_balance("0xdf77326E4BAEC32FC518e1F334b454eB4e3f4E89"))
print(w3.eth.get_balance("0x6EFEa917Df9A942A6Bd650d740F171BeD759F866"))