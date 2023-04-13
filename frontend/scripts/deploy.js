const hre = require("hardhat");


//The 'main' function to deploy contract locally
main = async () => {
    //Getting deployer's address
    const [deployer] = await hre.ethers.getSigners()

    //Getting deployer ETH balance
    const accountBalance = await deployer.getBalance()


    //Logging The Deployers's adddress and the balance
    console.log('Deploying Contracts Deployer Address ', deployer.address)
    console.log('Account Balance ', accountBalance.toString())


    //Deploying The Contract
    const contracts = await hre.ethers.getContractFactory('PickupLinesFactory')
    const contract = await contracts.deploy()
    await contract.deployed()

    //Logging the address of the deployed contract
    console.log('PickupLines Address ', contract.address)
}

//Handle error when run main function define try and catch block
const validateMain = async () => {
    try {
        await main()
        process.exit(0)
    } catch (err) {
        console.log(err)
        process.exit(1)
    }
}

//call validateMain function and validate Contract deploy or not
validateMain()