import React from 'react'
import {BrowserRouter, Routes,Route} from "react-router-dom"
import Layout from './hocs/Layout'
import About from './containers/About'
import Contact from './containers/Contact'
import Home from './containers/Home'
import ListingDetail from './containers/ListingDetail'
import Listings from './containers/Listings'
import Login from './containers/Login'
import SignUp from './containers/SignUp'
import NoteFound from './components/NoteFound'


const App = () => {
  return (
    <BrowserRouter>
    <Layout>
     <Routes>
        <Route   exact  path='/'  element={Home}/>
        <Route   exact  path='/about'  element={About}/>
        <Route   exact  path='/contact'  element={About}/>
        <Route   exact  path='/listings'  element={Listings}/>
        <Route   exact  path='/listings/:id'  element={ListingDetail}/>
        <Route   exact  path='/login'  element={Login}/>
        <Route   exact  path='/signup'  element={SignUp}/>
        <Route   exact  element={NoteFound}/>

     </Routes>
     </Layout>
    </BrowserRouter>
  )
}

export default App