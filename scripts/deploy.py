from brownie import FundMe, MockV3Aggregator, accounts, network, config
from scripts.helpfulScripts import getAccounts, deployMocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS



def deploy_fundMe():
    account=getAccounts()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        priceFeedAddress=config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deployMocks()
        priceFeedAddress=MockV3Aggregator[-1].address
    fund_me=FundMe.deploy(priceFeedAddress ,{"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to ${fund_me.address}")
    return fund_me

def main():
    deploy_fundMe()
