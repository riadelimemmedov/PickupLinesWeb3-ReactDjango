require("@nomiclabs/hardhat-waffle");
require('dotenv').config()

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.0",
  networks:{
    goerli:{
      url:process.env.GANACHE_NODE_URL,
      accounts:[process.env.METAMASK_PRIVATE_KEY]
    }
  }
};