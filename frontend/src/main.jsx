
//!React
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'

//!React Router
import { BrowserRouter, Routes, Route } from 'react-router-dom';


//?Custom Components
import PickupLine  from './routes/PickupLine.jsx'
import PickupForm  from './routes/PickupFormTest.jsx'
import Profile from './routes/Profile.jsx'


//*Main.jsx
ReactDOM.createRoot(document.getElementById('root')).render(
    <BrowserRouter>
        <Routes>
            <Route exact path="/" element={<App/>}/>
            <Route path="/create/pickup" element={<PickupForm/>}/>
            <Route path="/pickup/:pickuplines" element={<PickupLine/>}></Route>
            <Route path="/profile" element={<Profile/>}></Route>
        </Routes>
    </BrowserRouter>
)
