//!Web3
import web3 from "./web3"


//!Contract
import PickupLines from "../artifacts/contracts/PickupLines.sol/PickupLines.json"


//?export
export default (address) => {
    return new web3.eth.Contract(
        PickupLines.abi,
        address
    )
}