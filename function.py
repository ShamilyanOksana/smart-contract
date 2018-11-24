from web3 import Web3
from web3 import HTTPProvider
import web3.personal
import web3.contract
import web3.eth
import web3
import json
import solc


w3 = Web3(web3.HTTPProvider('http://127.0.0.1:8545'))
# contract_add = Web3.toChecksumAddress("0x088fb9f3e79fed60bd20752390eaa502071d339a")
contract_usr = Web3.toChecksumAddress("0xFeaB30128bC6a3BB840A80a7931Fe4ED58181fC9")
deflt = w3.eth.accounts[0]
w3.eth.defaultAccount = w3.eth.accounts[0]
a = web3.personal.Personal(w3).unlockAccount(contract_usr, "Drjfm1Px")
print(a)



contract_source_code = '''
pragma solidity ^0.4.21;

contract Greeter {
    string public greeting;

    function Greeter() public {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() view public returns (string) {
        return greeting;
    }
}
'''

compiled_sol = solc.compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:Greeter']


abi = [
	{
		"constant": False,
		"inputs": [
			{
				"name": "_greeting",
				"type": "string"
			}
		],
		"name": "setGreeting",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "greet",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "greeting",
		"outputs": [
			{
				"name": "",
				"type": "string"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	}
]

bytecode = json.dumps({
	"linkReferences": {},
	"object": "606060405260408051908101604052600381527f4b454b00000000000000000000000000000000000000000000000000000000006020820152600090805161004b9291602001906100a4565b50341561005757600080fd5b60408051908101604052600581527f48656c6c6f0000000000000000000000000000000000000000000000000000006020820152600090805161009e9291602001906100a4565b5061013f565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100e557805160ff1916838001178555610112565b82800160010185558215610112579182015b828111156101125782518255916020019190600101906100f7565b5061011e929150610122565b5090565b61013c91905b8082111561011e5760008155600101610128565b90565b61037f8061014e6000396000f3006060604052600436106100565763ffffffff7c0100000000000000000000000000000000000000000000000000000000600035041663a4136862811461005b578063cfae3217146100ae578063ef690cc014610138575b600080fd5b341561006657600080fd5b6100ac60046024813581810190830135806020601f8201819004810201604051908101604052818152929190602084018383808284375094965061014b95505050505050565b005b34156100b957600080fd5b6100c1610162565b60405160208082528190810183818151815260200191508051906020019080838360005b838110156100fd5780820151838201526020016100e5565b50505050905090810190601f16801561012a5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561014357600080fd5b6100c161020b565b600081805161015e9291602001906102a9565b5050565b61016a610327565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102005780601f106101d557610100808354040283529160200191610200565b820191906000526020600020905b8154815290600101906020018083116101e357829003601f168201915b505050505090505b90565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102a15780601f10610276576101008083540402835291602001916102a1565b820191906000526020600020905b81548152906001019060200180831161028457829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106102ea57805160ff1916838001178555610317565b82800160010185558215610317579182015b828111156103175782518255916020019190600101906102fc565b50610323929150610339565b5090565b60206040519081016040526000815290565b61020891905b80821115610323576000815560010161033f5600a165627a7a7230582011a9ed672084e011c9a61b4c869876c9b4e2edb7132d04d19a01cac56286f4ab0029",
	"opcodes": "PUSH1 0x60 PUSH1 0x40 MSTORE PUSH1 0x40 DUP1 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE PUSH1 0x3 DUP2 MSTORE PUSH32 0x4B454B0000000000000000000000000000000000000000000000000000000000 PUSH1 0x20 DUP3 ADD MSTORE PUSH1 0x0 SWAP1 DUP1 MLOAD PUSH2 0x4B SWAP3 SWAP2 PUSH1 0x20 ADD SWAP1 PUSH2 0xA4 JUMP JUMPDEST POP CALLVALUE ISZERO PUSH2 0x57 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH1 0x40 DUP1 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE PUSH1 0x5 DUP2 MSTORE PUSH32 0x48656C6C6F000000000000000000000000000000000000000000000000000000 PUSH1 0x20 DUP3 ADD MSTORE PUSH1 0x0 SWAP1 DUP1 MLOAD PUSH2 0x9E SWAP3 SWAP2 PUSH1 0x20 ADD SWAP1 PUSH2 0xA4 JUMP JUMPDEST POP PUSH2 0x13F JUMP JUMPDEST DUP3 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x1F ADD PUSH1 0x20 SWAP1 DIV DUP2 ADD SWAP3 DUP3 PUSH1 0x1F LT PUSH2 0xE5 JUMPI DUP1 MLOAD PUSH1 0xFF NOT AND DUP4 DUP1 ADD OR DUP6 SSTORE PUSH2 0x112 JUMP JUMPDEST DUP3 DUP1 ADD PUSH1 0x1 ADD DUP6 SSTORE DUP3 ISZERO PUSH2 0x112 JUMPI SWAP2 DUP3 ADD JUMPDEST DUP3 DUP2 GT ISZERO PUSH2 0x112 JUMPI DUP3 MLOAD DUP3 SSTORE SWAP2 PUSH1 0x20 ADD SWAP2 SWAP1 PUSH1 0x1 ADD SWAP1 PUSH2 0xF7 JUMP JUMPDEST POP PUSH2 0x11E SWAP3 SWAP2 POP PUSH2 0x122 JUMP JUMPDEST POP SWAP1 JUMP JUMPDEST PUSH2 0x13C SWAP2 SWAP1 JUMPDEST DUP1 DUP3 GT ISZERO PUSH2 0x11E JUMPI PUSH1 0x0 DUP2 SSTORE PUSH1 0x1 ADD PUSH2 0x128 JUMP JUMPDEST SWAP1 JUMP JUMPDEST PUSH2 0x37F DUP1 PUSH2 0x14E PUSH1 0x0 CODECOPY PUSH1 0x0 RETURN STOP PUSH1 0x60 PUSH1 0x40 MSTORE PUSH1 0x4 CALLDATASIZE LT PUSH2 0x56 JUMPI PUSH4 0xFFFFFFFF PUSH29 0x100000000000000000000000000000000000000000000000000000000 PUSH1 0x0 CALLDATALOAD DIV AND PUSH4 0xA4136862 DUP2 EQ PUSH2 0x5B JUMPI DUP1 PUSH4 0xCFAE3217 EQ PUSH2 0xAE JUMPI DUP1 PUSH4 0xEF690CC0 EQ PUSH2 0x138 JUMPI JUMPDEST PUSH1 0x0 DUP1 REVERT JUMPDEST CALLVALUE ISZERO PUSH2 0x66 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0xAC PUSH1 0x4 PUSH1 0x24 DUP2 CALLDATALOAD DUP2 DUP2 ADD SWAP1 DUP4 ADD CALLDATALOAD DUP1 PUSH1 0x20 PUSH1 0x1F DUP3 ADD DUP2 SWAP1 DIV DUP2 MUL ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP2 DUP2 MSTORE SWAP3 SWAP2 SWAP1 PUSH1 0x20 DUP5 ADD DUP4 DUP4 DUP1 DUP3 DUP5 CALLDATACOPY POP SWAP5 SWAP7 POP PUSH2 0x14B SWAP6 POP POP POP POP POP POP JUMP JUMPDEST STOP JUMPDEST CALLVALUE ISZERO PUSH2 0xB9 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0xC1 PUSH2 0x162 JUMP JUMPDEST PUSH1 0x40 MLOAD PUSH1 0x20 DUP1 DUP3 MSTORE DUP2 SWAP1 DUP2 ADD DUP4 DUP2 DUP2 MLOAD DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP DUP1 MLOAD SWAP1 PUSH1 0x20 ADD SWAP1 DUP1 DUP4 DUP4 PUSH1 0x0 JUMPDEST DUP4 DUP2 LT ISZERO PUSH2 0xFD JUMPI DUP1 DUP3 ADD MLOAD DUP4 DUP3 ADD MSTORE PUSH1 0x20 ADD PUSH2 0xE5 JUMP JUMPDEST POP POP POP POP SWAP1 POP SWAP1 DUP2 ADD SWAP1 PUSH1 0x1F AND DUP1 ISZERO PUSH2 0x12A JUMPI DUP1 DUP3 SUB DUP1 MLOAD PUSH1 0x1 DUP4 PUSH1 0x20 SUB PUSH2 0x100 EXP SUB NOT AND DUP2 MSTORE PUSH1 0x20 ADD SWAP2 POP JUMPDEST POP SWAP3 POP POP POP PUSH1 0x40 MLOAD DUP1 SWAP2 SUB SWAP1 RETURN JUMPDEST CALLVALUE ISZERO PUSH2 0x143 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST PUSH2 0xC1 PUSH2 0x20B JUMP JUMPDEST PUSH1 0x0 DUP2 DUP1 MLOAD PUSH2 0x15E SWAP3 SWAP2 PUSH1 0x20 ADD SWAP1 PUSH2 0x2A9 JUMP JUMPDEST POP POP JUMP JUMPDEST PUSH2 0x16A PUSH2 0x327 JUMP JUMPDEST PUSH1 0x0 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 ISZERO PUSH2 0x200 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x1D5 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x200 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x1E3 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP SWAP1 POP JUMPDEST SWAP1 JUMP JUMPDEST PUSH1 0x0 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 PUSH1 0x1F ADD PUSH1 0x20 DUP1 SWAP2 DIV MUL PUSH1 0x20 ADD PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE DUP1 SWAP3 SWAP2 SWAP1 DUP2 DUP2 MSTORE PUSH1 0x20 ADD DUP3 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV DUP1 ISZERO PUSH2 0x2A1 JUMPI DUP1 PUSH1 0x1F LT PUSH2 0x276 JUMPI PUSH2 0x100 DUP1 DUP4 SLOAD DIV MUL DUP4 MSTORE SWAP2 PUSH1 0x20 ADD SWAP2 PUSH2 0x2A1 JUMP JUMPDEST DUP3 ADD SWAP2 SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 JUMPDEST DUP2 SLOAD DUP2 MSTORE SWAP1 PUSH1 0x1 ADD SWAP1 PUSH1 0x20 ADD DUP1 DUP4 GT PUSH2 0x284 JUMPI DUP3 SWAP1 SUB PUSH1 0x1F AND DUP3 ADD SWAP2 JUMPDEST POP POP POP POP POP DUP2 JUMP JUMPDEST DUP3 DUP1 SLOAD PUSH1 0x1 DUP2 PUSH1 0x1 AND ISZERO PUSH2 0x100 MUL SUB AND PUSH1 0x2 SWAP1 DIV SWAP1 PUSH1 0x0 MSTORE PUSH1 0x20 PUSH1 0x0 KECCAK256 SWAP1 PUSH1 0x1F ADD PUSH1 0x20 SWAP1 DIV DUP2 ADD SWAP3 DUP3 PUSH1 0x1F LT PUSH2 0x2EA JUMPI DUP1 MLOAD PUSH1 0xFF NOT AND DUP4 DUP1 ADD OR DUP6 SSTORE PUSH2 0x317 JUMP JUMPDEST DUP3 DUP1 ADD PUSH1 0x1 ADD DUP6 SSTORE DUP3 ISZERO PUSH2 0x317 JUMPI SWAP2 DUP3 ADD JUMPDEST DUP3 DUP2 GT ISZERO PUSH2 0x317 JUMPI DUP3 MLOAD DUP3 SSTORE SWAP2 PUSH1 0x20 ADD SWAP2 SWAP1 PUSH1 0x1 ADD SWAP1 PUSH2 0x2FC JUMP JUMPDEST POP PUSH2 0x323 SWAP3 SWAP2 POP PUSH2 0x339 JUMP JUMPDEST POP SWAP1 JUMP JUMPDEST PUSH1 0x20 PUSH1 0x40 MLOAD SWAP1 DUP2 ADD PUSH1 0x40 MSTORE PUSH1 0x0 DUP2 MSTORE SWAP1 JUMP JUMPDEST PUSH2 0x208 SWAP2 SWAP1 JUMPDEST DUP1 DUP3 GT ISZERO PUSH2 0x323 JUMPI PUSH1 0x0 DUP2 SSTORE PUSH1 0x1 ADD PUSH2 0x33F JUMP STOP LOG1 PUSH6 0x627A7A723058 KECCAK256 GT 0xa9 0xed PUSH8 0x2084E011C9A61B4C DUP7 SWAP9 PUSH23 0xC9B4E2EDB7132D04D19A01CAC56286F4AB002900000000 ",
	"sourceMap": "28:310:0:-;;;52:30;;;;;;;;;;;;;;;;-1:-1:-1;;52:30:0;;;;;;;;;:::i;:::-;;91:63;;;;;;;;128:18;;;;;;;;;;;;;;;;-1:-1:-1;;128:18:0;;;;;;;;;:::i;:::-;;28:310;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;-1:-1:-1;28:310:0;;;-1:-1:-1;28:310:0;:::i;:::-;;;:::o;:::-;;;;;;;;;;;;;;;;;;;;:::o;:::-;;;;;;;"
}).encode()



cntrct = w3.eth.contract(abi=abi,bytecode=bytecode)

# web3.miner.Miner(w3).start(1)
# th = cntrct.constructor().transact()
# tx_receipt = w3.eth.waitForTransactionReceipt(th)
# web3.miner.Miner(w3).stop()

#tx_hash = cntrct.constructor().transact()
# greeter = w3.eth.contract(
#     address=tx_receipt.contractAddress,
#     abi=abi,
# )
#
# l = w3.eth.getCode(tx_receipt.contractAddress)
#
# print('Default contract greeting: {}'.format(
#     greeter.functions.greet().call()
# ))

# tx = {"value": "0",
#         "parameters": [],
#         "abi": "0x99ff0d9125e1fc9531a11262e15aeb2c60509a078c4cc4c64cefdfb06ff68647",
#         "contractName": "Register",
#         "bytecode": "608060405234801561001057600080fd5b5061039b806100206000396000f3006080604052600436106100565763ffffffff7c01000000000000000000000000000000000000000000000000000000006000350416633c077a48811461005b5780639e6ce89f146100f2578063acd107561461014f575b600080fd5b34801561006757600080fd5b50610073600435610176565b6040518080602001838152602001828103825284818151815260200191508051906020019080838360005b838110156100b657818101518382015260200161009e565b50505050905090810190601f1680156100e35780820380516001836020036101000a031916815260200191505b50935050505060405180910390f35b3480156100fe57600080fd5b506040805160206004803580820135601f810184900484028501840190955284845261014d943694929360249392840191908190840183828082843750949750509335945061025f9350505050565b005b34801561015b57600080fd5b506101646102d0565b60408051918252519081900360200190f35b60606000808381548110151561018857fe5b90600052602060002090600202016000016000848154811015156101a857fe5b906000526020600020906002020160010154818054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561024f5780601f106102245761010080835404028352916020019161024f565b820191906000526020600020905b81548152906001019060200180831161023257829003601f168201915b5050505050915091509150915091565b60408051808201909152828152602080820183905260008054600181018083559180528351805192949360029092027f290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e56301926102be92849201906102d7565b50602082015181600101555050505050565b6000545b90565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061031857805160ff1916838001178555610345565b82800160010185558215610345579182015b8281111561034557825182559160200191906001019061032a565b50610351929150610355565b5090565b6102d491905b80821115610351576000815560010161035b5600a165627a7a72305820f7026957157229d202664f211d5ae737b25732be1e86718dea3e8873a1652afa0029",
#         "linkReferences": {},
#         "name": "",
#         "inputs": "()",
#         "type": "constructor",
#         "from": "account{0}"}
# # web3.contract.Contract().web3 = w3
# web3.contract.ContractFunctions(abi=abi, web3=w3)
# # web3.eth.Eth(w3).contract()


# reg = web3.eth.Eth(w3).contract(contract_add)
# reg.functions.addHuman("Oksana", 20).call()
# num = reg.functions.numbertHuman().call()
# print(num)

