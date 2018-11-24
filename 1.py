from web3 import Web3
from web3 import HTTPProvider
import web3.personal
import web3.contract
import web3.eth
import web3
import json
from solc import compile_source



w3 = Web3(HTTPProvider('http://192.168.0.2:8545'))

contract_source_code = '''pragma solidity ^0.4.0;

contract Register {
    
    struct human {
        string name;
        uint age;
    }
    human[] people;
    uint ind;
    
    function addHuman(string newName, uint newAge){
        people.push(human(newName, newAge));
    }
    
    function numbertHuman() returns(uint number){
        return people.length;
    }
    
    function getAll(uint number) returns (string, uint){
        return(people[number].name, people[number].age);
    }
    
}'''

# web3.py instance
# w3 = Web3(Web3.EthereumTesterProvider())

# compiled_sol = compile_source(contract_source_code)# Compiled source code
# contract_interface = compiled_sol['<stdin>:Register']

web_eth = web3.eth.Eth(w3)
# web_eth.defaultAccount = "0xfeab30128bc6a3bb840a80a7931fe4ed58181fc9"
web_eth.defaultAccount = web_eth.accounts[0]
web_eth.defaultBlock = "latest"

print(web_eth.defaultAccount)
print(web_eth.accounts[0])
abi = [
	{
		"constant": False,
		"inputs": [
			{
				"name": "number",
				"type": "uint256"
			}
		],
		"name": "getAll",
		"outputs": [
			{
				"name": "",
				"type": "string"
			},
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"name": "newName",
				"type": "string"
			},
			{
				"name": "newAge",
				"type": "uint256"
			}
		],
		"name": "addHuman",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [],
		"name": "numbertHuman",
		"outputs": [
			{
				"name": "number",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
byt = json.dumps({
	"linkReferences": {},
	"object": "608060405234801561001057600080fd5b5061039b806100206000396000f3006080604052600436106100565763ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416633c077a48811461005b5780639e6ce89f146100f2578063f50c7ef31461014f575b600080fd5b34801561006757600080fd5b50610073600435610176565b6040518080602001838152602001828103825284818151815260200191508051906020019080838360005b838110156100b657818101518382015260200161009e565b50505050905090810190601f1680156100e35780820380516001836020036101000a031916815260200191505b50935050505060405180910390f35b3480156100fe57600080fd5b506040805160206004803580820135601f810184900484028501840190955284845261014d943694929360249392840191908190840183828082843750949750509335945061025f9350505050565b005b34801561015b57600080fd5b506101646102d0565b60408051918252519081900360200190f35b60606000808381548110151561018857fe5b90600052602060002090600202016000016000848154811015156101a857fe5b906000526020600020906002020160010154818054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561024f5780601f106102245761010080835404028352916020019161024f565b820191906000526020600020905b81548152906001019060200180831161023257829003601f168201915b5050505050915091509150915091565b60408051808201909152828152602080820183905260008054600181018083559180528351805192949360029092027f290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e56301926102be92849201906102d7565b50602082015181600101555050505050565b6000545b90565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061031857805160ff1916838001178555610345565b82800160010185558215610345579182015b8281111561034557825182559160200191906001019061032a565b50610351929150610355565b5090565b6102d491905b80821115610351576000815560010161035b5600a165627a7a72305820b448cfc24446aa982e21485b9ce2cf7417583486d099c757245bcc98589b177e0029",
	"opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x39B DUP1 PUSH2 0x20 PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN STOP PUSH1 0x80 PUSH1 0x40 MSTORE PUSH1 0x4 CALLDATASIZE LT PUSH2 0x56 JUMPI PUSH4 0xFFFFFFFF PUSH29 0x100000000000000000000000000000000000000000000000000000000 PUSH1 0x0 CALLDATALOAD DIV AND PUSH4 0x3C077A48 DUP2 EQ PUSH2 0x5B JUMPI DUP1 PUSH4 0x9E6CE89F EQ PUSH2 0xF2 JUMPI DUP1 PUSH4 0xF50C7EF3 EQ PUSH2 0x14F JUMPI JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0x67 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x73 PUSH1 0x4 CALLDATALOAD PUSH2 0x176 JUMP JUMPDEST PUSH1 0x40 MLOAD DUP1 DUP1 PUSH1 0x20 ADD DUP4 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP2 SUB DUP3 MSTORE DUP5 DUP2 DUP2 MLOAD DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP DUP1 MLOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP1 DUP4 DUP4 PUSH1 0x0 JUMPDEST DUP4 DUP2 LT ISZERO PUSH2 0xB6 JUMPI DUP2 DUP2 ADD MLOAD DUP4 DUP3 ADD MSTORE PUSH1 0x20 ADD PUSH2 0x9E JUMP JUMPDEST POP POP POP POP SWAP1 POP SWAP1 DUP2 ADD SWAP1 PUSH1 0x1F AND DUP1 ISZERO PUSH2 0xE3 JUMPI DUP1 DUP3 SUB DUP1 MLOAD PUSH1 0x1 DUP4 PUSH1 0x20 SUB PUSH2 0x100 EXP SUB NOT AND DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP JUMPDEST POP SWAP4 POP POP POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0xFE JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x40 DUP1 MLOAD PUSH1 0x20 PUSH1 0x4 DUP1 CALLDATALOAD DUP1 DUP3 ADD CALLDATALOAD PUSH1 0x1F DUP2 ADD DUP5 SWAP1 DIV DUP5 MUL DUP6 ADD DUP5 ADD SWAP1 SWAP6 MSTORE DUP5 DUP5 MSTORE PUSH2 0x14D SWAP5 CALLDATASIZE SWAP5 SWAP3 SWAP4 PUSH1 0x24 SWAP4 SWAP3 DUP5 ADD SWAP2 SWAP1 DUP2 SWAP1 DUP5 ADD DUP4 DUP3 DUP1 DUP3 DUP5 CALLDATACOPY POP SWAP5 SWAP8 POP POP SWAP4 CALLDATALOAD SWAP5 POP PUSH2 0x25F SWAP4 POP POP POP POP JUMP JUMPDEST STOP JUMPDEST CALLVALUE DUP1 ISZERO PUSH2 0x15B JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH2 0x164 PUSH2 0x2D0 JUMP JUMPDEST PUSH1 0x40 DUP1 MLOAD SWAP2 DUP3 MSTORE MLOAD SWAP1 DUP2 SWAP1 SUB PUSH1 0x20 ADD SWAP1 RETURN JUMPDEST PUSH1 0x60 PUSH1 0x0 DUP1 DUP4 DUP2 SLOAD DUP2 LT ISZERO ISZERO PUSH2 0x188 JUMPI INVALID JUMPDEST SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x2 MUL ADD PUSH1 0x0 ADD PUSH1 0x0 DUP5 DUP2 SLOAD DUP2 LT ISZERO ISZERO PUSH2 0x1A8 JUMPI INVALID JUMPDEST SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x2 MUL ADD PUSH1 0x1 ADD SLOAD DUP2 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 ISZERO PUSH2 0x24F JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x224 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x24F JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x232 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP SWAP2 POP SWAP2 POP SWAP2 POP SWAP2 POP SWAP2 JUMP JUMPDEST PUSH1 0x40 DUP1 MLOAD DUP1 DUP3 ADD SWAP1 SWAP2 MSTORE DUP3 DUP2 MSTORE PUSH1 0x20 DUP1 DUP3 ADD DUP4 SWAP1 MSTORE PUSH1 0x0 DUP1 SLOAD PUSH1 0x1 DUP2 ADD DUP1 DUP4 SSTORE SWAP2 DUP1 MSTORE DUP4 MLOAD DUP1 MLOAD SWAP3 SWAP5 SWAP4 PUSH1 0x2 SWAP1 SWAP3 MUL PUSH32 0x290DECD9548B62A8D60345A988386FC84BA6BC95484008F6362F93160EF3E563 ADD SWAP3 PUSH2 0x2BE SWAP3 DUP5 SWAP3 ADD SWAP1 PUSH2 0x2D7 JUMP JUMPDEST POP PUSH1 0x20 DUP3 ADD MLOAD DUP2 PUSH1 0x1 ADD SSTORE POP POP POP POP POP JUMP JUMPDEST PUSH1 0x0 SLOAD JUMPDEST SWAP1 JUMP JUMPDEST DUP3 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x1F ADD PUSH1 0x20 SWAP1 DIV DUP2 ADD SWAP3 DUP3 PUSH1 0x1F LT PUSH2 0x318 JUMPI DUP1 MLOAD PUSH1 0xFF NOT AND DUP4 DUP1 ADD OR DUP6 SSTORE PUSH2 0x345 JUMP JUMPDEST DUP3 DUP1 ADD PUSH1 0x1 ADD DUP6 SSTORE DUP3 ISZERO PUSH2 0x345 JUMPI SWAP2 DUP3 ADD JUMPDEST DUP3 DUP2 GT ISZERO PUSH2 0x345 JUMPI DUP3 MLOAD DUP3 SSTORE SWAP2 PUSH1 0x20 ADD SWAP2 SWAP1 PUSH1 0x1 ADD SWAP1 PUSH2 0x32A JUMP JUMPDEST POP PUSH2 0x351 SWAP3 SWAP2 POP PUSH2 0x355 JUMP JUMPDEST POP SWAP1 JUMP JUMPDEST PUSH2 0x2D4 SWAP2 SWAP1 JUMPDEST DUP1 DUP3 GT ISZERO PUSH2 0x351 JUMPI PUSH1 0x0 DUP2 SSTORE PUSH1 0x1 ADD PUSH2 0x35B JUMP STOP LOG1 PUSH6 0x627A7A723058 KECCAK256 0xb4 0x48 0xcf 0xc2 DIFFICULTY 0x46 0xaa SWAP9 0x2e 0x21 0x48 JUMPDEST SWAP13 0xe2 0xcf PUSH21 0x17583486D099C757245BCC98589B177E0029000000 ",
	"sourceMap": "25:453:0:-;;;;8:9:-1;5:2;;;30:1;27;20:12;5:2;25:453:0;;;;;;;"
}).encode()

sender = web3.contract.ContractConstructor(w3, abi, byt)
tx = web3.contract.Contract(w3).call().get()
print(tx)
# web_eth.sendTransaction(tx)

# sender.transact(tx)


# tx_reciept = web3.eth.wait_for_transaction_receipt(w3, tx_hash)
# print(tx_reciept)
# my_contract = web3.eth.Eth(w3).contract(address=tx_reciept.)
