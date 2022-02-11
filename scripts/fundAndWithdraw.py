from brownie import FundMe
from scripts.helpfulScripts import getAccounts

def fund():
    fund_me=FundMe[-1]
    account = getAccounts()
    entranceFee = fund_me.getEntranceFee()
    print(f"current entry fee is {entranceFee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entranceFee})
def withdraw():
    fund_me=FundMe[-1]
    account=getAccounts()
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()
    