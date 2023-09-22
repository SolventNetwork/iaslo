from ape import accounts, project, networks

"""
For testing purposes, launch ganache-cli with the following command:

ganache-cli -m "ring ring ring ring ring ring ring banana phone ring ring ring"

The seed phrase guarantees the same addresses are generated every time so we
can hardcode the addresses in our tests. Also necessary the first time you run
this:

ape accounts import --use-mnemonic banana

And input the seed phrase above.
"""

account = accounts.load("banana")


def deploy_erc20_token(name, symbol):
    TestToken = project.TestToken
    deployed_token = account.deploy(TestToken, name, symbol)
    print(f"Deployed Token at address: {deployed_token.address}")
    return deployed_token


def deploy_uniswap_v4_contracts():
    UniswapV4Factory = project.contracts["UniswapV4Factory"]
    factory = account.deploy(UniswapV4Factory)
    print(f"Deployed Uniswap V4 Factory at address: {factory.address}")
    return factory


def test_stuff():
    print(f"Deploying contracts with account: {account.address}")
    print(f"Account balance: {account.balance}")
    print(f"Connected to {networks.network.name}")
    print(dir(project.dependencies["OpenZeppelin"]["master"]))

    token1 = deploy_erc20_token("token1", "TKN1")
    token2 = deploy_erc20_token("token2", "TKN2")

    # uniswap_factory = deploy_uniswap_v4_contracts()

    print(f"Deployed Token1 at address: {token1.address}")
    print(f"Deployed Token2 at address: {token2.address}")
    # print(f"Deployed Uniswap V4 Factory at address: {uniswap_factory.address}")
