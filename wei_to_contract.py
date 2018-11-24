from web3 import Web3
from web3 import HTTPProvider
import web3.personal
import web3.contract
import web3.eth
import web3
import json
import time


abi = "[{\"constant\":true,\"inputs\":[{\"name\":\"number\",\"type\":\"uint256\"}],\"name\":\"getAll\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"},{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"newName\",\"type\":\"string\"},{\"name\":\"newAge\",\"type\":\"uint256\"}],\"name\":\"addHuman\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"numberHuman\",\"outputs\":[{\"name\":\"number\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"}]"
bytecode = "608060405234801561001057600080fd5b5061044a806100206000396000f3fe608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680633c077a481461005c5780639e6ce89f14610117578063acd10756146101e9575b600080fd5b34801561006857600080fd5b506100956004803603602081101561007f57600080fd5b8101908080359060200190929190505050610214565b6040518080602001838152602001828103825284818151815260200191508051906020019080838360005b838110156100db5780820151818401526020810190506100c0565b50505050905090810190601f1680156101085780820380516001836020036101000a031916815260200191505b50935050505060405180910390f35b34801561012357600080fd5b506101e76004803603604081101561013a57600080fd5b810190808035906020019064010000000081111561015757600080fd5b82018360208201111561016957600080fd5b8035906020019184600183028401116401000000008311171561018b57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803590602001909291905050506102fd565b005b3480156101f557600080fd5b506101fe61036d565b6040518082815260200191505060405180910390f35b60606000808381548110151561022657fe5b906000526020600020906002020160000160008481548110151561024657fe5b906000526020600020906002020160010154818054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102ed5780601f106102c2576101008083540402835291602001916102ed565b820191906000526020600020905b8154815290600101906020018083116102d057829003601f168201915b5050505050915091509150915091565b600060408051908101604052808481526020018381525090806001815401808255809150509060018203906000526020600020906002020160009091929091909150600082015181600001908051906020019061035b929190610379565b50602082015181600101555050505050565b60008080549050905090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106103ba57805160ff19168380011785556103e8565b828001600101855582156103e8579182015b828111156103e75782518255916020019190600101906103cc565b5b5090506103f591906103f9565b5090565b61041b91905b808211156104175760008160009055506001016103ff565b5090565b9056fea165627a7a72305820f9907a556ab1df6407ce2dae467081c4917775e8df8fed76a7349b04a6c03c1a0029"


w3 = Web3(web3.HTTPProvider('http://127.0.0.1:8545'))
contract_adr = Web3.toChecksumAddress("0xBe43136C7FfFfd74d8Ad6dBf4D66e93432F15ea7")

contract_usr = Web3.toChecksumAddress("0xFeaB30128bC6a3BB840A80a7931Fe4ED58181fC9")
contract_usr2 = Web3.toChecksumAddress("0xde2a9e3fba487cc473f18a7375c6f6f057bc3c5e")

deflt = w3.eth.accounts[0]
w3.eth.defaultAccount = w3.eth.accounts[0]
a = web3.personal.Personal(w3).unlockAccount(contract_usr, "Drjfm1Px")
print(a)
# b = web3.personal.Personal(w3).unlockAccount(contract_usr2, "123456789")
# print(b)
w3.miner.start(1)
# tx = w3.eth.sendTransaction({"from":contract_usr, "to":contract_usr2, "value": 10})
tx = w3.contract(contract_adr, abi=abi).sendTransaction({'from': contract_usr}).transfer(contract_adr, 10)
w3.eth.waitForTransactionReceipt(tx)
w3.miner.stop()
balance = w3.eth.getBalance(contract_adr)
print(balance)
balance_acc = w3.eth.getBalance(contract_usr)
print(balance_acc)

