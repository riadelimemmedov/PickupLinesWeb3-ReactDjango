//!React
import { useState } from 'react';


//!React Toastify
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


//!CSSTransition
import { CSSTransition } from 'react-transition-group';

//!MaterialUI
import {
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
    TextField,
} from '@material-ui/core';
import Typography from '@mui/material/Typography';


//!modal.css
import '../modal.css'



//?LoginRegisterForm
const LoginRegisterForm = () => {
    const [open, setOpen] = useState(true);
    const [isWantRegister,setRegister] = useState(false)
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [repassword,setRePassword] = useState('')
    const [metamaskAddress, setMetamaskAddress] = useState('');



    //rePasswordStyle
    const rePasswordStyle = {
        display: isWantRegister ? 'block' : 'none'
    }

    //registerButtonStyle
    const registerButtonStyle = {
        fontSize:'18px',
        fontWeight:'bold',
        marginRight: isWantRegister ? '290px' : '255px'
    }

    //*handleUser
    const handleUser = (event) => {
        event.preventDefault();
        if(!username || !email || !password || !metamaskAddress){
            toast.error("Please fill in all required fields")
            return
        }
        if(password !== repassword & isWantRegister==true){
            toast.error('Password do not match')
            return
        }
        if (!/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email)) {
            toast.error('Please enter a valid email address.');
            return;
        }

        if(!/^0x[a-fA-F0-9]{40}$/.test(metamaskAddress)){
            console.log('Metamask address type ', metamaskAddress)
            toast.error('Plase enter a valid metamask key')
            return
        }
        else{
            if(isWantRegister){
                toast.success('Created account successfully')
                return
            }
            else if(!isWantRegister){
                toast.success('Is logged in to account successfully')
                return
            }
        }
    }


    //*handleRegister
    const handleRegister = (event) => {
        if(isWantRegister){
            setRegister(false)
        }
        else if(isWantRegister == false){
            setRegister(true)
        }
    }

    //*handleSubmit
    const handleSubmit = (event) => {
        event.preventDefault();
        // Handle form submission
    };

    //*handleClose
    const handleClose = () => {
        setOpen(false);
    };

    //return jsx to UI
    return (
        <>
        <ToastContainer/>
        <Dialog open={open} style={{width:'100%'}} className="register-dialog">
            <CSSTransition in={open} timeout={300} classNames="fade">
                <div>
                    <DialogTitle><b>Register Or Logged In Account</b></DialogTitle>
                    <form onSubmit={handleSubmit}>
                        <DialogContent>
                            <TextField
                                autoFocus
                                margin="dense"
                                label="Username"
                                value={username}
                                onChange={(event) => setUsername(event.target.value)}
                                fullWidth
                            />
                            <TextField
                                margin="dense"
                                label="Email"
                                value={email}
                                onChange={(event) => setEmail(event.target.value)}
                                fullWidth
                            />
                            <TextField
                                margin="dense"
                                label="Password"
                                type="password"
                                value={password}
                                onChange={(event) => setPassword(event.target.value)}
                                fullWidth
                            />
                            <TextField
                                style={rePasswordStyle}
                                margin="dense"
                                label="Repassword"
                                type="password"
                                value={repassword}
                                onChange={(event) => setRePassword(event.target.value)}
                                fullWidth
                            />
                            <TextField
                                margin="dense"
                                label="Metamask Address"
                                value={metamaskAddress}
                                onChange={(event) => setMetamaskAddress(event.target.value)}
                                fullWidth
                            />
                        </DialogContent>
                        <DialogActions>
                            <Typography style={registerButtonStyle} color="primary">
                                <Button variant='contained' type='button' style={{background:'#218838',color:'#fff'}} onClick={handleRegister}>
                                    {
                                        isWantRegister ? <Typography>Login</Typography> : <Typography>Register</Typography>
                                    }
                                </Button>
                            </Typography>
                            <Button variant='contained' onClick={handleClose}>Cancel</Button>
                            <Button variant='contained' type="submit" color="primary" onClick={handleUser}>
                                Create
                            </Button>
                        </DialogActions>
                    </form>
                </div>
            </CSSTransition>
        </Dialog>
        </>
    );
}
export default LoginRegisterForm