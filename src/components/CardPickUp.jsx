//!React
import { useState,useEffect } from 'react'
import * as React from 'react';


//!MaterialUI
import {AppBar,CssBaseline,Grid,Toolbar,Container,Button,Menu} from '@material-ui/core'
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import CardActions from '@mui/material/CardActions';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ShareIcon from '@mui/icons-material/Share';
import { red } from '@mui/material/colors';
import { shadows } from '@mui/system';
import ThumbUpAltIcon from '@mui/icons-material/ThumbUpAlt';
import ThumbDownAltIcon from '@mui/icons-material/ThumbDownAlt';


//!React Router
import {Link} from 'react-router-dom'


//!Web3
import web3 from "../../contracts/web3.js"


//?CardPick
const CardPickUp = (props) => {

    const {address:pickupline_address,author:pickupline_author,timestamp:pickupline_timestamp} = props.address_author_timestamp
    
    return(
        <>
        <Grid item key={1} xs={12} sm={2} md={4} style={{marginTop:'40px'}}>
            <Card sx={{ maxWidth: 345,boxShadow: 3 }} style={{marginTop:'20px'}}>
                <CardHeader
                    avatar={
                        <Avatar src={`https://api.dicebear.com/6.x/avataaars/svg?seed=Garfield=${pickupline_author}`}>
                        ID
                        </Avatar>
                    }
                    action={
                        <IconButton aria-label="settings">
                            <MoreVertIcon />
                        </IconButton>
                    }
                    title={`${pickupline_author}`}
                    subheader={`${new Date(pickupline_timestamp*1000).toLocaleString()}`}
                />
                <Link to={`/pickup/${pickupline_address}`}>
                    <CardMedia
                        component="img"
                        height="300"
                        image={`https://api.dicebear.com/5.x/thumbs/svg?seed=${pickupline_address}`}
                        alt="Not Found Image"
                    />
                </Link>
                
                <CardActions disableSpacing>
                    <IconButton aria-label="add to favorites">
                        <FavoriteIcon />
                    </IconButton>
                    <IconButton aria-label="share">
                        <ThumbUpAltIcon />
                    </IconButton>
                    
                </CardActions>
            </Card>
        </Grid>
    </>
    )
}

export default CardPickUp
