
from brownie import config, network, accounts, MockV3Aggregator

DECIMALS=8
STARTING_PRICE=200000000000

FORKED_LOCAL_ENVIRONMENTS=["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development", "ganache-local"]

def getAccounts():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
def deployMocks():
    print(f"network is ${network.show_active()}")
    print("Deploying Mocks")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": getAccounts()})
    print("mocks deployed")