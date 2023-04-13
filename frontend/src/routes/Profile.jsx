//!React
import React from 'react';


//!MateriUI Component
import { makeStyles } from '@material-ui/core/styles';
import CardMedia from '@material-ui/core/CardMedia';
import CloudUploadIcon from '@material-ui/icons/CloudUpload';
import CardActions from '@mui/material/CardActions';
import { Card, CardContent, Typography, TextField, Button,List,ListItem,ListItemText } from '@material-ui/core';
import Container from '@mui/material/Container';
import CssBaseline from '@mui/material/CssBaseline';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import { shadows } from '@mui/system';


//!Custom Components
import Navbar from './NavbarPickup'


//!useStyles
import useStyles from "../styles"


//?UserProfileCard
const UserProfileCard = () => {

    //classes
    const classes = useStyles();

    return (
        <>
            <Navbar/>
                <Box sx={{flexGrow:1}}>
                    <Grid container spacing={2} item xs={12}>
                            <Grid item xs={4}>
                                <Card className={classes.rootProfile} style={{width:'100%',marginLeft:'150px'}} sx={{boxShadow:3}}>
                                    <CardMedia
                                        className={classes.mediaProfile}
                                        image="https://api.dicebear.com/6.x/avataaars/svg?seed=Garfield=$0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"
                                        title="User Avatar"
                                    />
                                    <CardContent>
                                        <Typography gutterBottom variant="h5" component="h2">
                                        John Doe
                                        </Typography>
                                        <Typography variant="body2" color="textSecondary" component="p">
                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                                        </Typography>
                                        <Button
                                        variant="contained"
                                        color="default"
                                        startIcon={<CloudUploadIcon />}
                                        >
                                        Upload Image
                                        </Button>
                                    </CardContent>
                                </Card>
                            </Grid>
                            <Grid item xs={4}>
                                <Card style={{ width: '100%', margin: 'auto', marginTop: '64px' }} sx={{boxShadow:3}}>
                                    <CardContent>
                                    <Typography variant="h6">Account Details</Typography>
                                    <form>
                                        <TextField fullWidth label="Address" margin="normal" />
                                        <TextField label="First Name" margin="normal" /><br/>
                                        <TextField label="Last Name" margin="normal" />
                                        <TextField fullWidth label="Email Address" margin="normal" />
                                        <TextField label="Date Joined" margin="normal" /><br/>
                                        <Button variant="contained" color="primary" style={{ marginTop: '20px',width:'100%' }}>
                                        Save
                                        </Button>
                                    </form>
                                    </CardContent>
                                </Card>
                            </Grid>
                            <Grid item xs={4}>
                                <Card style={{ width:'100%',height:'600px',marginTop:'64px' }}>
                                        <CardMedia
                                            className={classes.mediaProfile}
                                            image="https://api.dicebear.com/6.x/avataaars/svg?seed=Garfield=$0x3C44CdDdB6a900fa2b585dd299e03d12F"
                                            title="green iguana"
                                            />
                                        <CardContent>
                                        <Typography gutterBottom variant="h5" component="div">
                                            Lizard
                                        </Typography>
                                        <Typography variant="body2" color="primary">
                                            Lizards are a widespread group of squamate reptiles, with over 6,000
                                            species, ranging across all continents except Antarctica
                                        </Typography>
                                        </CardContent>
                                        <CardActions>
                                        <Button size="small">Share</Button>
                                        <Button size="small">Learn More</Button>
                                        </CardActions>
                                    </Card>
                            </Grid>
                    </Grid>
            </Box>
        </>
    );
}

export default UserProfileCard;
