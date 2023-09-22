pragma solidity ^0.8.0;

import "@openzeppelin/token/ERC20/ERC20.sol";

contract TestToken is ERC20 {
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply if needed
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }
}
