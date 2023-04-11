//!Web3
import web3 from "./web3"


//!Contract
import PickupLinesFactory from "../artifacts/contracts/PickupLines.sol/PickupLinesFactory.json"


const instance = new web3.eth.Contract(
    PickupLinesFactory.abi,
    import.meta.env.VITE_CONTRACT_ADDRESS
)

console.log('PickupLinesFactory Contract Here ', instance)
console.log('Adress PickupLinesFactory ', instance.options.address)
console.log('Methods PickupLinesFactory ', instance.methods)


export default instance