// SPDX-License-Identifier: UNLICENSED

//Define Solidity Version Top Of The Project
pragma solidity ^0.8.0;

//Use JavaScript Console in Solidity File For Debugging Project
import "hardhat/console.sol";


//PickupLinesFactory
contract PickupLinesFactory{
    address[] public deployedPickup;
    uint[] public createdDatePick;
    address[] public authorPickup;

    
    function createPickup() public{
        address newPickup = address(new PickupLines());
        deployedPickup.push(newPickup);
        createdDatePick.push(block.timestamp);
        authorPickup.push(msg.sender);
    }

    function getDeployedPickup() public view returns(address[] memory){
        return deployedPickup;
    }
    
    function getCreatedDatePickup() public view returns(uint[] memory){
        return createdDatePick;
    }

    function getPickupCount() public view returns(uint){
        return deployedPickup.length;
    }

    function getAuthorPickup() public view returns(address[] memory){
        return authorPickup;
    }

    function getPickupAtIndex() public view returns(address){
        require(deployedPickup.length>0,"Not found pickup in list");
        return deployedPickup[deployedPickup.length-1];
    }

}

//Main Solidity Contract
contract PickupLines{
    //Solidity event,that fires when a new line is submitted
    event NewPickUpLine(address indexed from,uint256 timestamp,string line);

    //Data Members
    uint256 private seed;//seed data
    uint256 totalLines;//total lines data
    mapping (address => bool) hasWrote;//map of all addresses with line submit to blockchain


    //Each PickupLine Object Define Using struct keyword at solidity 
    struct Pickup {
        address writer;
        string line;
        uint256 timestamp;
    }

    //Array of all pick up lines submitted
    Pickup[] public pickups;


    //Constructor Function For Our Contract
    constructor() payable{
        console.log('Work Constructor File For PickupLines Contract');
    }


    //Function for adding a new line to the contract
    function newLine(string memory _line) public{
        //Adding a new Pickup to our blockchain
        totalLines+=1;
        pickups.push(Pickup(msg.sender,_line,block.timestamp));
        hasWrote[msg.sender] = true;
        emit NewPickUpLine(msg.sender,block.timestamp,_line);//like as logging when user send to blockchain write data to emit object
    }

    //Function to get all the lines submitted to the contract
    function getTotalLines() public view returns(uint256){
        console.log('We have %s total PickUp ', totalLines);
        return totalLines;
    }
}

