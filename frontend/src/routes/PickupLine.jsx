
//!React
import React, { useState,useEffect,useRef } from "react";
import { useParams } from 'react-router-dom';


//!MateriUI Component
import { styled } from '@mui/material/styles';
import { shadows } from '@mui/system';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@material-ui/core/CardContent';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Typography from '@mui/material/Typography';
import CircularProgress from '@material-ui/core/CircularProgress';


//!React Toastify
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


//!Third Party Package
import ReCAPTCHA from 'react-google-recaptcha';
import axios from 'axios';


//!Abi and Custom Function
import PickupLines from "../../artifacts/contracts/PickupLines.sol/PickupLines.json"
import PickupLinesFactory from "../../artifacts/contracts/PickupLines.sol/PickupLinesFactory.json"

import pickup_lines_factory from "../../contracts/pickup_lines_factory.js"
import pickup_lines from "../../contracts/pickup_lines.js"


//!Web3
import web3 from "../../contracts/web3.js"


//!useStyles
import useStyles from '../styles.js'




//?PickupLine
const PickupLine = () => {
    const captchaRef = useRef(null);

    const [lineDescription,setLineDescription] = useState("")
    const [allPickUps,setAllPickUps] = useState([])
    const [isLoading,setIsLoading] = useState(false)
    
    let { pickuplines } = useParams()
    const pickuLinespObj = pickup_lines(pickuplines)
    const classes = useStyles()


    //*createPickupLine
    const createPickupLine = async(event) => {
        event.preventDefault()
        if(typeof window !== "undefined" && typeof window.ethereum !== "undefined"){
            try{
                    setIsLoading(true)
                    const accounts = await web3.eth.getAccounts()
                    const createdPickupLines = await pickuLinespObj.methods.newLine(lineDescription).send({from:accounts[0]})
                    console.log('Succsesfully create createdPickupLines ', createdPickupLines)
                        setTimeout(()=>{
                            setIsLoading(false)
                            window.location.reload()   
                        },3000)
            }
            catch(err){
                setTimeout(()=>{
                    setIsLoading(false)   
                    toast.error('When create pickup error')
                },3000)
            }
        }
        else{
            console.log('Not fount metamask account')
        }
    }

    
    //*getAllPickups
    const getAllPickups = async () => {
        const count_pickups = await pickuLinespObj.methods.getTotalLines().call()
        const pickups = await Promise.all(
            Array(parseInt(count_pickups))
                .fill()
                .map((element,index) => {
                    return pickuLinespObj.methods.pickups(index).call()
                })
        )
        setAllPickUps(Object.values(pickups))
    }   


    //?Item
    const Item = styled(Paper)(({ theme }) => ({
        backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#ced6e0',
        ...theme.typography.body2,
        padding: theme.spacing(1),
        textAlign: 'center',
        color: theme.palette.text.secondary,
    }));

    
    //?useEffect
    useEffect(()=>{
        getAllPickups()
    },[])

    return(
        <>
        <ToastContainer/>
        <Typography variant="h5">Pickups List</Typography>
        {import.meta.env.VITE_CONTRACT_ADDRESS}
        <hr/>
        <Box sx={{flexGrow:1,marginTop:'80px'}}>
                <Card sx={{maxWidth:1258,boxShadow:3}} style={{marginBottom:'20px'}}>
                    <CardContent>
                        Pickuplines Address <Typography variant="h6" color="textSecondary">{pickuplines}</Typography>
                    </CardContent>
                </Card>

                <Card style={{padding:'6px',marginTop:'-110px',height:'210px',marginLeft:'1265px',position:'sticky',top:'15px'}} sx={{boxShadow:3}}>
                    <CardContent>
                            <form onSubmit={createPickupLine}>
                                <TextField
                                    label="Line Text"
                                    variant="outlined"
                                    fullWidth
                                    onChange={(e)=>{setLineDescription(e.target.value)}}
                                    value={lineDescription}
                                    required
                                />
                                <Button type="submit" variant="contained" color="secondary" style={{marginLeft:'400px',marginTop:'15px',width:'180px'}} disabled={isLoading}>
                                    {isLoading ? <CircularProgress size={24}/> : 'Create New Pickup'}
                                </Button>
                            </form>
        
                            <ReCAPTCHA sitekey={import.meta.env.VITE_CAPTCHA_SITE_KEY} ref={captchaRef}/>

                    </CardContent>
                </Card>
                

                <Grid container spacing={2} sm={8}>
                    {
                        Object.values(allPickUps).map((data,index)=>(
                            <Grid item xs={4} sm={6} key={index}>
                                <Item>Item {index+1}</Item>
                                    <Card className={classes.rootcard} sx={{maxWidth:650,marginTop:'10px',boxShadow:3}}>
                                        <CardContent>
                                            <Typography gutterBottom variant="h6" component="h2">
                                                Writer : <span style={{color:'#546de5'}}>{data.writer}</span>
                                            </Typography>
                                            <Typography  variant="h6" component="h2">
                                                Line Description : <span style={{color:'#546de5'}}>{data.line}</span>
                                            </Typography>
                                            <Typography variant="h6" component="h2">
                                                Created Time : <span style={{color:'#546de5'}}>
                                                    {new Date(data.timestamp*1000).toLocaleString()}
                                                </span> 
                                            </Typography>
                                        </CardContent>
                                    </Card>
                            </Grid>
                        ))
                    }
                </Grid>
        </Box>   
        </>
    )
}
export default PickupLine