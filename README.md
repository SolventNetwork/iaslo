# Interest Accruing Stop Loss Orders (IASLO)

This contract is designed as a hook on Uniswap v4 to allow users to open stop loss orders. The stop loss orders lock up liquidity so that they can always be filled. To compensate for this lockup, liquidity providers are compensated with a flow of interest from the order. There can also be additional interest paid to an external source (e.g. lenders in a lending protocol).

To test the protocol, make sure you have a local instance of Ganache. Run it with
```
ganache-cli
```
then open a new terminal window.

Compile the contracts with
```
ape compile --include-dependencies
```
and run the test script with
```
ape run scripts/deploy_test.py
```

## Contribution Guidelines

See our [contribution guidelines](/CONTRIBUTING.md)!