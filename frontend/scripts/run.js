//*The main function to run contract locally for an instance

const hre = require("hardhat");

const main = async () => {
    //Helper function to get the contract 'PickupLines'
    const contracts = await hre.ethers.getContractFactory('PickupLines') //getContractFactory => returns a JavaScript object that objects represents a smart contract factory.You can use this object to deploy new instance ofthe smart contract


    //Deploying the smart contract for an contract instance
    const contract = await contracts.deploy()
    await contract.deployed() //contract is deployed or not if deploy succsessfully deployed code

    console.log('Deployed Contract Address ', contract.address) //0x5FbDB2315678afecb367f032d93F642f64180aa3
}


//Define try & catch block for main function handling if occur error when running the code
const validateMain = async () => {
    try {
        await main()
        console.log('Main functio calling inside try block')
        process.exit(0) // => 0 means end the process without any kind of failure and terminate block node
    } catch (err) {
        console.log('When Deploy Contract Occur Error ', err)
        process.exit(1) // => 1 means end the process with some failure for example(Uncaught Fatal Exception) popular error when runnning javascript code at node.js environment
    }
}

//call validateMain functio and deploy contract
validateMain()