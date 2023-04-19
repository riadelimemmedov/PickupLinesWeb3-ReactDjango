
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
let totalNewLine=0;
let allPickupLines;
let pickupLinesAddress;



//beforeEach => run this function when run test each time
beforeEach(async()=> {
    accounts = await web3.eth.getAccounts() 

    pickup_lines_factory = await new web3.eth.Contract(compiledPickupLinesFactory.abi)
        .deploy({data:compiledPickupLinesFactory.bytecode})
        .send({from:accounts[0],gas:'4712388'})


    await pickup_lines_factory.methods.createPickup().send({
        from:accounts[1],
        gas:'4712388'
    });

    
    await pickup_lines_factory.methods.createPickup().send({
        from:accounts[1],
        gas:'4712388'
    });


    allPickupLines = await pickup_lines_factory.methods.getDeployedPickup().call();
    [pickupLinesAddress] = await pickup_lines_factory.methods.getDeployedPickup().call()
    pickup_lines = await new web3.eth.Contract(
        compiledPickupLines.abi,
        pickupLinesAddress
    )

})


//describe => use for to group a number of test
describe('PickupLinesFactory and Pickuplines',()=>{

    it('Return all fake accounts from ganache',async()=>{
        assert(accounts.length > 0,'Not found fake accoount yet')
    })

    it('Contract is deployed or not succsesfully',async()=>{
        assert.ok(pickup_lines_factory.options.address)
        assert.ok(pickup_lines.options.address)
    })
    
    it('Return all deployed pickuplines', async()=>{
        const last_pickuplines = await pickup_lines_factory.methods.getPickupAtIndex().call()
        assert.equal(last_pickuplines,Object.values(allPickupLines).pop())
    })

    it('Created newLine succsesfully or not',async()=>{
        const nl = await pickup_lines.methods.newLine('Hello,how are you?').send({from:accounts[2],gas:'4712388'})
        totalNewLine+=1
        assert.equal(nl.status,true,'Error when deploying newLine')
    })

    it('Return TotalDeployedPickupLines From Contract',async()=>{
        assert(totalNewLine>0,'Not found newLine, newLine value is 0')
    })
})