
//!React
import { useState,useEffect } from 'react'
import * as React from 'react';


//!Css
import './App.css'
import "./Pagination.css"
import 'react-toastify/dist/ReactToastify.css';


//!MaterialUI
import {AppBar,CssBaseline,Grid,Toolbar,Container,Button,Menu} 
from '@material-ui/core'
import { styled } from '@mui/material/styles';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Collapse from '@mui/material/Collapse';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import { red } from '@mui/material/colors';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ShareIcon from '@mui/icons-material/Share';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import {PhotoCamera,PostAdd} from '@material-ui/icons'
import PersonIcon from '@mui/icons-material/Person';
import MuiAlert from '@mui/material/Alert';
import Box from '@mui/material/Box';
import { shadows } from '@mui/system';


//!React Router
import {Link} from 'react-router-dom'


//!Custom Components
import CardPickUp from './components/CardPickUp'
import Navbar from './routes/NavbarPickup.jsx'




//!Third Party Package
import { ToastContainer, toast } from 'react-toastify';
import ReactPaginate from 'react-paginate';


//!useStyles
import useStyles from './styles'


//!Web3
import web3 from "../contracts/web3.js"


//!Abi and Custom Function
import PickupLines from "../artifacts/contracts/PickupLines.sol/PickupLines.json"
import PickupLinesFactory from "../artifacts/contracts/PickupLines.sol/PickupLinesFactory.json"

import pickup_lines_factory from "../contracts/pickup_lines_factory.js"
import pickup_lines from "../contracts/pickup_lines.js"


//?App
function App() {
  //State variable to store the account connected with the wallet
  const [currentAccount,setCurrentAccount] = useState("")
  const [pickuplinesCount,setPickuplinesCount] = useState("")
  const [deployedPickups,getDeployedPickups] = useState([])
  const [currentPage, setCurrentPage] = useState(0);

  const [deployedContractAddress,setDeployedAddress] = useState("")

  const itemsPerPage = 3; // Number of items per page
  const startIndex = currentPage * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;

  console.log('StartIndex Value ', startIndex)

  const paginatedItems = deployedPickups.slice(startIndex, endIndex); // Array of items for the current page

  
    //*connectWallet    
    //Function to connect the wallet
    const connectWallet = async() => {
      try{
          const { ethereum } = window
          if(!ethereum){
              alert("Get MetaMask")
              return
          }
          else{
              const accounts = await ethereum.request({method:'eth_requestAccounts'})
              console.log('Connected ', accounts[0])
              setCurrentAccount(accounts[0])
          }
          }
      catch(err){
          console.log(err)
      }
  }


    //*checkIfWalletIsConnected
    //Function to the check if the wallet is connected to the app
      const checkIfWalletIsConnected = async() => {
        try{
            const { ethereum } = window
            if(!ethereum){
                alert("Make sure you have metamask")
                return
            }
            else{
                console.log('We have the ethereum object')
        }

        const accounts = await ethereum.request({ method: "eth_accounts" })
        if(accounts.length !== 0){
            const account = accounts[0]
            console.log('Found an authorized account ', account)
            setCurrentAccount(account)
        }
        else{
            console.log('Your metamask account not login to this site,please login if you want to use this site properly')
            toast.error('No authorized account found')
        }

        }
        catch(err){
            console.log(err)
        }
  }



    //*handlePageChange
    const handlePageChange = ({ selected }) => {
      setCurrentPage(selected);
    };


    //*renderPickups
    const renderPickups = async() => {
      const deployed_list_pickups = await pickup_lines_factory.methods.getDeployedPickup().call()
      const created_date_list_pickups = await pickup_lines_factory.methods.getCreatedDatePickup().call()
      const pickups_author = await pickup_lines_factory.methods.getAuthorPickup().call()

      console.log('All author list created pickups ', pickups_author)

      const deployed_pickups = deployed_list_pickups.map((el,index)=>[el,pickups_author[index],created_date_list_pickups[index]])

      console.log('Length of deployed pickuops ', deployed_pickups.length)

      getDeployedPickups(deployed_pickups)
    }


    //*renderDeployedPickupsCount
    const renderDeployedPickupsCount = async() => {
      const deployed_pickups_count = await pickup_lines_factory.methods.getPickupCount().call()    
      setPickuplinesCount(deployed_pickups_count)
    }



    //*pickup
    const createPickupLinesFactory = async () => {
      try{
        if(typeof window !== "undefined" && typeof window.ethereum !== "undefined"){
          const account = await web3.eth.getAccounts()
          // console.log('Account List ', account)

          // const contract_pickuplines_factory = new web3.eth.Contract(PickupLinesFactory.abi,"0x5FbDB2315678afecb367f032d93F642f64180aa3")
          // console.log('PickupLinesFactory Contract Here ', contract_pickuplines_factory)
          // // console.log('Adress PickupLinesFactory ', contract_pickuplines_factory.options.address)
          // console.log('Methods PickupLinesFactory ', contract_pickuplines_factory.methods)

          const contract_pickuplines = await pickup_lines_factory.methods.createPickup().send({from:account[2]})
          console.log('Create PickupLines succsesfully ', contract_pickuplines)
          
          
          const pickupValueForIndex = await pickup_lines_factory.methods.getPickupAtIndex().call()
          console.log('pickupValueForIndex ', pickupValueForIndex)


          const [pickUpLineAddress] =  await pickup_lines_factory.methods.getDeployedPickup().call()
          console.log('All pickups adress ', await pickup_lines_factory.methods.getDeployedPickup().call())
          console.log('PickupLine Adress ', pickUpLineAddress)


          const blockNumber = await web3.eth.getBlockNumber(console.log)
          console.log('Block Number ', blockNumber)

          console.log('--------------------------------------------------------------------------------------------------------------------------------')


          const pickuplines = new web3.eth.Contract(PickupLines.abi,pickUpLineAddress)
          console.log('Pickuplines Createad Succsesfully', pickuplines)
          console.log('Adress Pickuplines ', pickuplines.options.address)
          console.log('Methods Pickuplines ', pickuplines.methods)
          

          // //Get the count of all lines before adding a new line
          // let count = await pickuplines.methods.getTotalLines().call()
          // console.log('Without toNumber ', count)

          // const createdPickupLines = await pickuplines.methods.newLine('Hey,hey,how are you?').send({from:account[0]})
          // console.log('Create Pickuplines Succsesfully ', createdPickupLines)

          // let totalPickupLines = await pickuplines.methods.getTotalLines().call()
          // console.log('Without toNumber ', totalPickupLines)

          let totalPickupFactory = await pickup_lines_factory.methods.getPickupCount().call()
          setPickuplinesCount(totalPickupFactory)

          const deployed_list_pickups = await pickup_lines_factory.methods.getDeployedPickup().call()
          const created_date_list_pickups = await pickup_lines_factory.methods.getCreatedDatePickup().call()
          const pickups_author = await pickup_lines_factory.methods.getAuthorPickup().call()

          const deployed_pickups = deployed_list_pickups.map((el,index)=>[el,pickups_author[index],created_date_list_pickups[index]])


          getDeployedPickups(deployed_pickups)

          console.log('totalPickupFactory', totalPickupFactory)

        }
      }
      catch(err){ 
        console.log('What happing here...')
        console.log('Err value when call pickup ', err)
        alert('When create pickups lines occur something')
      }
    }


    //*notify
    const notify = () => toast.info(`Find ${pickuplinesCount} pickups`)
  


    //?useEffect
    //React hook to check for wallet connection when the app is mounted
    useEffect(()=>{
      renderPickups()
      checkIfWalletIsConnected()
      renderDeployedPickupsCount()
    },[])
    
    
    //useStyles
    const classes = useStyles()



  //return JSX
  return(
      <>
        <CssBaseline/>
        <Navbar connectWallet={connectWallet} checkIfWalletIsConnected={checkIfWalletIsConnected} currentAccount={currentAccount}/>
          <Container className={classes.cardGrid} maxWidth="md">
              {
                paginatedItems?.length > 0 ?
                  ( 
                    <>
                      <Grid container spacing={4}>
                      {paginatedItems.map((pickupline,index)=>(
                        <CardPickUp address_author_timestamp={{address:pickupline[0],author:pickupline[1],timestamp:pickupline[2]}}  key={index}/>
                      ))}
                    </Grid>
                    <ReactPaginate
                        pageCount={endIndex < pickuplinesCount ? pickuplinesCount/3 : ''} // Total number of pages
                        pageRangeDisplayed={3} // Number of pages to display in the pagination
                        marginPagesDisplayed={2} // Number of pages to display before and after the current page
                        onPageChange={handlePageChange} // Callback function to handle page changes
                        containerClassName={'pagination'} // CSS class for the pagination container
                        activeClassName={'active'} 
                        disabled={true}
                      />
                    </>
                  )
                : (<>
                      <Box className={classes.cartMessageRoot} sx={{boxShadow:3}}>
                        <Typography className={classes.cartMessageTitle} variant="h6">Not Found Last Hours Pickups Lines</Typography>
                      </Box>
                    </>
                  )
              }


              <div>
                  <button onClick={notify}>Notify!</button>
                  {
                    currentAccount !== "" ? (
                      <Button variant="contained" style={{marginLeft:'646px',marginTop:'10px',textTransform:'capitalize'}} sx={{boxShadow:3}} onClick={createPickupLinesFactory}>
                        Create PickupLines Factory
                      </Button>
                    )
                    :
                    (
                      <ToastContainer/>
                    )
                  }
              </div>
          </Container>
  </>
  )
}
export default App
