import React from 'react';
import { useState,useEffect } from 'react'

import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { shadows } from '@mui/system';
import Typography from '@mui/material/Typography';


import useStyles from '../styles.js'


const hello = () => {
    const classes = useStyles()

    const [cardData, setCardData] = useState({
        cardNumber: "",
        cardHolder: "",
        expirationDate: "",
        cvv: "",
        });
    
        const handleChange = (event) => {
        const { name, value } = event.target;
        setCardData((prevCardData) => ({
            ...prevCardData,
            [name]: value,
        }));
        };
    
        const handleSubmit = (event) => {
        event.preventDefault();
        console.log(cardData);
        };

    return(
    <Card className={classes.root}>
        <CardContent>
        <Typography className={classes.title}>Enter Card sDetails</Typography>
            <form className={classes.form} onSubmit={handleSubmit}>
            <TextField
                className={classes.formInput}
                label="Card Number"
                name="cardNumber"
                value={cardData.cardNumber}
                onChange={handleChange}
                required
            />
            <TextField
                className={classes.formInput}
                label="Card Holder Name"
                name="cardHolder"
                value={cardData.cardHolder}
                onChange={handleChange}
                required
            />
            <TextField
                className={classes.formInput}
                label="Expiration Date"
                name="expirationDate"
                value={cardData.expirationDate}
                onChange={handleChange}
                required
            />
            <TextField
                className={classes.formInput}
                label="CVV"
                name="cvv"
                value={cardData.cvv}
                onChange={handleChange}
                required
            />
            <Button
                variant="contained"
                color="primary"
                type="submit"
                className={classes.submitButton}
            >
                Submit
            </Button>
            </form>
        </CardContent>
        </Card>
    );
    
}
export default hello