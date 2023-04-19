//!React
import React,{useState,useEffect} from "react"


//!MaterialUI
import {AppBar,CssBaseline,Grid,Toolbar,Container,Button,Menu} from '@material-ui/core'
import Avatar from '@mui/material/Avatar';
import Typography from '@mui/material/Typography';
import PersonIcon from '@mui/icons-material/Person';


//!React Router
import {Link} from 'react-router-dom'


//!Third Party Package
import { ToastContainer, toast } from 'react-toastify';


//!useStyles
import useStyles from "../styles"


import { wallet_requestPermissions } from '@metamask/detect-provider';
import { ethers } from 'ethers';
import web3 from "../../contracts/web3.js"




//?Navbar
const Navbar = ({connectWallet,checkIfWalletIsConnected,currentAccount,setCurrentAccount}) => {
    //useStyles
    const classes = useStyles()

    return(
        <>
            <AppBar position="relative" className={classes.navbar}>
                <Toolbar>
                    <Link to="/" style={{textDecoration:'none'}}>
                        <Avatar 
                        className={classes.avatar} 
                        src="https://images.unsplash.com/photo-1523961131990-5ea7c61b2107?ixlib=rb-4.0.3ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074q=80">
                        </Avatar>
                    </Link>
                    <Typography variant="h6">PickUpLines</Typography>

                    {
                        currentAccount !== "" ? (
                            <>
                                <Link to="/profile" style={{textDecoration:'none',marginLeft:'25px'}}>
                                    <Button variant="outlined" startIcon={<PersonIcon/>} className={classes.create_pickup}>
                                    Profile
                                    </Button>
                                </Link>
                                <div style={{marginLeft:'20px'}}>
                                    Already Logged In
                                </div>
                            </>
                        )
                        :(
                            <Button onClick={connectWallet} variant="outlined" className={classes.connect_metamask} disabled={currentAccount != '' ? true : false}>Connect Metamask</Button>
                        )
                    }
                </Toolbar>
            </AppBar>
        </>
    )
}
export default Navbar