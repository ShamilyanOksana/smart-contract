from web3 import Web3
from web3 import HTTPProvider
import web3.personal
import web3.contract
import web3.eth
import web3
import json
from solc import compile_source



w3 = Web3(HTTPProvider('http://192.168.0.2:8545'))
ac = web3.eth.Eth(w3).accounts
print(ac)