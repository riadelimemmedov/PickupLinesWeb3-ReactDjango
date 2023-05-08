import { useState } from 'react';
    import {
    Button,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
    TextField,
    } from '@material-ui/core';


//!LoginRegisterForm
const LoginRegisterForm = () => {
    const [open, setOpen] = useState(true);
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [metamaskAddress, setMetamaskAddress] = useState('');


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
        <Dialog open={open}>
            <DialogTitle><b>Create Account Or Logged In Account</b></DialogTitle>
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
                            margin="dense"
                            label="Metamask Address"
                            value={metamaskAddress}
                            onChange={(event) => setMetamaskAddress(event.target.value)}
                            fullWidth
                        />
                    </DialogContent>
                    <DialogActions>
                        <Button onClick={handleClose}>Cancel</Button>
                        <Button type="submit" color="primary">
                            Create
                        </Button>
                    </DialogActions>
                </form>
        </Dialog>
        </>
    );
}
export default LoginRegisterForm