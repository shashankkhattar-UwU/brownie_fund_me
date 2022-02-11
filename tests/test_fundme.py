from scripts.helpfulScripts import getAccounts, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fundMe
from brownie import network, accounts, exceptions
import pytest


def test_can_fund_and_withdraw():
    account=getAccounts()
    fund_me=deploy_fundMe()
    entranceFee=fund_me.getEntranceFee()+100
    tx=fund_me.fund({"from": account, "value": entranceFee})
    tx.wait(1)
    assert fund_me.addressToAmount(account.address)==entranceFee
    tx2=fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmount(account.address)==0
    
def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    account=getAccounts()
    fund_me=deploy_fundMe()
    badActor=accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": badActor})
    
    