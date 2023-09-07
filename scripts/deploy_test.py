from ape import accounts, project

# Load the default account
account = accounts[0]


def deploy_erc20_token():
    # Access the ERC20 contract from the OpenZeppelin dependency
    ERC20 = project.dependencies["OpenZeppelin"]["master"].ERC20
    deployed_token = account.deploy(ERC20)
    return deployed_token


def deploy_uniswap_v4_contracts():
    # Assuming UniswapV4Factory, UniswapV4Pool, etc. are the main contract names
    UniswapV4Factory = project.contracts["UniswapV4Factory"]
    factory = account.deploy(UniswapV4Factory)
    return factory


def main():
    token1 = deploy_erc20_token()
    token2 = deploy_erc20_token()

    uniswap_factory = deploy_uniswap_v4_contracts()

    print(f"Deployed Token1 at address: {token1.address}")
    print(f"Deployed Token2 at address: {token2.address}")
    print(f"Deployed Uniswap V4 Factory at address: {uniswap_factory.address}")
