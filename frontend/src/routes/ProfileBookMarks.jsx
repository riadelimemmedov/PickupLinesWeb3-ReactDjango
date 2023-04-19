import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Grid, Paper, Typography } from '@material-ui/core';


import Navbar from './../components/NavbarPickup';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    padding: theme.spacing(2),
    backgroundColor: '#F7F9FC',
    marginTop:'20px'
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    backgroundColor: '#FFFFFF',
    boxShadow: '0px 2px 6px rgba(0, 0, 0, 0.15)',
  },
  title: {
    color: '#172B4D',
    marginBottom: theme.spacing(2),
  },
  subtitle: {
    color: '#6B778C',
    marginBottom: theme.spacing(1),
  },
  link: {
    color: '#172B4D',
    textDecoration: 'none',
    '&:hover': {
      textDecoration: 'underline',
    },
  },
  image: {
    width: '100%',
    height: 'auto',
    borderRadius: theme.spacing(1),
    marginBottom: theme.spacing(1),
  },
}));

const BookmarkPage = () => {
  const classes = useStyles();

  return (
    <>
    <Navbar/>
    <div className={classes.root}>
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Typography variant="h4" gutterBottom className={classes.title}>
            My Bookmarks
          </Typography>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Paper className={classes.paper}>
            <img src="https://picsum.photos/id/237/300/200" alt="Google" className={classes.image} />
            <Typography variant="h5" gutterBottom className={classes.title}>
              Google
            </Typography>
            <Typography variant="subtitle1" gutterBottom className={classes.subtitle}>
              The most popular search engine
            </Typography>
            <Typography variant="body2">
              <a href="https://www.google.com/" className={classes.link}>https://www.google.com/</a>
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Paper className={classes.paper}>
            <img src="https://picsum.photos/id/238/300/200" alt="Material UI" className={classes.image} />
            <Typography variant="h5" gutterBottom className={classes.title}>
              Material UI
            </Typography>
            <Typography variant="subtitle1" gutterBottom className={classes.subtitle}>
              React components for faster and easier web development
            </Typography>
            <Typography variant="body2">
              <a href="https://material-ui.com/" className={classes.link}>https://material-ui.com/</a>
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Paper className={classes.paper}>
            <img src="https://picsum.photos/id/239/300/200" alt="GitHub" className={classes.image} />
            <Typography variant="h5" gutterBottom className={classes.title}>
              GitHub
            </Typography>
            <Typography variant="subtitle1" gutterBottom className={classes.subtitle}>
              The world's leading software development platform
            </Typography>
            <Typography variant="body2">
              <a href="https://github.com/" className={classes.link}>https://github.com/</a>
            </Typography>
        </Paper>
        </Grid>
        </Grid>
    </div>
    </>
)}
export default BookmarkPage