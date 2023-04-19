
//!Import Required Packages
const assert = require('assert')
const ganache = require('ganache-cli')
const Web3 = require('web3')


//!Deploy Ganache At Web3 and Create web3 instance
const web3 = new Web3(ganache.provider())



//!Abi and Custom Function
const compiledPickupLinesFactory = require("../artifacts/contracts/PickupLines.sol/PickupLinesFactory.json")
const compiledPickupLines = require("../artifacts/contracts/PickupLines.sol/PickupLines.json")


//*define required variables for testing process
let accounts;
let pickup_lines_factory;
let pickup_lines;
let pickup_lines_address;



//beforeEach => run this function when run test each time
beforeEach(async()=> {
    accounts = await web3.eth.getAccounts() 
})


//describe => use for to group a number of test
describe('PickupLinesFactory and Pickuplines',()=>{
    it('return all accounts from ganache',async()=>{
        console.log('Accounts is ', accounts)
    })
})