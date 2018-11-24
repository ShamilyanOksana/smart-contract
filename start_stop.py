import web3.miner
import web3.personal
import web3.eth
import time
provider = web3.HTTPProvider('http://127.0.0.1:8545')
# provider = web3.HTTPProvider('http://192.168.0.2:8545')
w3 = web3.Web3(provider)
web3.miner.Miner(w3).start(1)
time.sleep(5)
web3.miner.Miner(w3).stop()
# a = web3.personal.Personal(w3).unlockAccount(web3.eth.Eth(w3).accounts[4], "123456789")
# print(a)
