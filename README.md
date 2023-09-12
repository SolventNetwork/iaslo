# Interest Accruing Stop Loss Orders (IASLO)

This contract is designed as a hook on Uniswap v4 to allow users to open stop loss orders. The stop loss orders lock up liquidity so that they can always be filled. To compensate for this lockup, liquidity providers are compensated with a flow of interest from the order. There can also be additional interest paid to an external source (e.g. lenders in a lending protocol).

## Contribution Guidelines

See our [contribution guidelines](/CONTRIBUTING.md)!

## Getting Started

### MacOS

To get started, first clone this repo by running the following terminal commands:

```
git clone https://github.com/SolventNetwork/iaslo
cd iaslo
```

Then create and activate your Python virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

Next, install the Node.js packages. If you don't have Node.js and npm installed, you can download and install them from [the official Node.js website](https://nodejs.org/).

```
npm install
```

This will read the `package.json` and `package-lock.json` files in the directory, automatically installing the necessary Node.js packages into `node_modules`.

### Windows

To get started on Windows, first clone this repo by running the following command prompt commands:

```
git clone https://github.com/SolventNetwork/iaslo
cd iaslo
```

Then create and activate your Python virtual environment:

```
python -m venv .venv
.venv\Scripts\activate
```

Next, install the Node.js packages. If you don't have Node.js and npm installed, you can download and install them from [the official Node.js website](https://nodejs.org/).

```
npm install
```

This will read the `package.json` and `package-lock.json` files in the directory, automatically installing the necessary Node.js packages into `node_modules`.

## Testing

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
