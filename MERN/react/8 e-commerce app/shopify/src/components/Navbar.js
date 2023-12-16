import { Link, NavLink, Outlet } from "react-router-dom";
import './Navbar.css'
export default function Navbar() {
   return (
      <>
      <div>
         <nav className="navbar navbar-expand-lg bg-body-tertiary">
            <div className="container-fluid">
               <Link to={'/home'} className="navbar-brand" href="#"><i className="bi bi-shop"></i>&nbsp; Shopify</Link>
               <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span className="navbar-toggler-icon"></span>
               </button>
               <div className="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul className="navbar-nav mb-2 mb-lg-0 ms-auto">
                     <li className="nav-item ">
                        <NavLink to={'/home'} className="nav-link" aria-current="page" >Home</NavLink>
                     </li>
                     <li className="nav-item ">
                        <NavLink to={'/products'} className="nav-link" aria-current="page" >Products</NavLink>
                     </li>
                     <li className="nav-item ">
                        <NavLink to={'/contact'} className="nav-link" aria-current="page" >Contact</NavLink>
                     </li>  
                  </ul>   
               </div>
            </div>
         </nav>
      </div>
      <Outlet/>
      </>
      

   )
}
