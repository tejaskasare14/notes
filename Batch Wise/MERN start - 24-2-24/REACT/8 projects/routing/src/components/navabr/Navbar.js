import React from 'react'
import './navbar.css'
import { Link, NavLink } from 'react-router-dom'

export default function Navbar() {
  return (
    <div className='navbar'>
      <nav>
        <h1>Reat Routing</h1>

        <NavLink to="/home">Home</NavLink>
        <NavLink to="/product">Product</NavLink>
        <NavLink to="/contact">Contact</NavLink>
      </nav>
    </div>
  )
}
