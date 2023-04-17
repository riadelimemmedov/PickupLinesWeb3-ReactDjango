import {
    makeStyles
} from '@material-ui/core/styles'

const useStyles = makeStyles((theme) => ({
    avatar: {
        marginRight: '10px'
    },
    connect_metamask: {
        marginLeft: 'auto',
        fontWeight: 'italic',
        backgroundColor: '#DEFCF9',
        textTransform: 'capitalize'
    },
    create_pickup: {
        marginLeft: '1400px',
        backgroundColor: '#DA7F8F',
        fontWeight: 'italic',
        textTransform: 'capitalize'
    },
    navbar: {
        backgroundColor: '#7286D3',
    },
    cardGrid: {
        paddingTop: '20px 0px'
    },
    root: {
        minWidth: 275,
        maxWidth: 500,
        margin: "auto",
        marginTop: 50,
    },
    title: {
        fontSize: 24,
        fontWeight: "bold",
        marginBottom: 16,
    },
    form: {
        display: "flex",
        flexDirection: "column",
        alignItems: "flex-start",
        marginTop: 16,
    },
    formInput: {
        marginBottom: 16,
        width: "100%",
    },
    submitButton: {
        marginTop: 16,
        alignSelf: "flex-end",
    },
    rootcard: {
        maxWidth: 345,
    },
    media: {
        height: 140,
    },
    cartMessageRoot:{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '25px',
        backgroundColor: '#CCE5FF',
        borderRadius: '5px',
        marginTop:'60px',
    },
    cartMessageTitle : {
        fontWeight: 'bold',
        marginBottom: '10px',
    },
    cartMessageText:{
        textAlign: 'center',
    },


    //Profile
    rootProfile: {
        maxWidth: 345,
        marginTop:80,
        marginLeft:50
    },
    mediaProfile: {
        height: 0,
        paddingTop: '90%',
         // 16:9
    },
    userPickupLines:{
        paddingTop:'500px',
        backgroundSize:'100%',
        borderRadius:'10px',
    },
    cardGridProfile:{
        paddingTop:'20px 0px'
    },
    favorite_pickuplinesProfile:{
        maxWidth:275
    },
    listProfile:{
        marginTop:100
    }
}))
export default useStyles