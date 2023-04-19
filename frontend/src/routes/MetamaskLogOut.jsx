//!React
import React,{useState,useEffect} from "react";


//!React Toastify
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


//!Web3
import Web3 from 'web3';

import Navbar from "../components/NavbarPickup";


//?PickupLogOut
const PickupLogOut = ({connectWallet,checkIfWalletIsConnected,currentAccountl,setCurrentAccount}) => {

    useEffect(() => {
        async function init() {
            if (window.ethereum) {
                try {
                    // Listen for accountsChanged event
                    window.ethereum.on('accountsChanged', handleAccountsChanged);
                } 
                catch (error) {
                    toast.error("Not Logged In User,Please Connect User Account To Metamask")
                }
            } 
            else {
                console.log('Metamask not found');
                toast.info("Please Install Metamask To Browser")
            }
            }
            init();
    }, []);

    const handleAccountsChanged = (newAccounts) => {
        // Check if user has disconnected their account
        console.log('Handled account ', newAccounts)
        if(newAccounts.length !== 0){
            toast.promise(
                connectWallet(),
                {
                    pending:'Logged In Plese Wait One Minute...',
                    success: 'Logged Successfully To Metamask',
                    error:'When you are Logged In Occur Error',
                }
            ).finally(()=>console.log('Finish Process'))

        }
        else if (newAccounts.length === 0) {
            // Handle lock event
            setCurrentAccount("")
            toast.info("Successfully Logged Out")
        } 
        // else {//If user change metamask account work this code block automatically
        //     // Update accounts state
        //     setCurrentAccount(newAccounts);
        //         toast.info("Change Account Successfully")
        //     }
    };
};

export default PickupLogOut;