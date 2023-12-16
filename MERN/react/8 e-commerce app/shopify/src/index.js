import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.min.css'
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import ErrorPage from './pages/ErrorPage';
import Home from './pages/Home';
import Contact from './pages/Contact';
import Product from './pages/Product';
import ProductDetails from './components/products/ProductDetails';

const routes = createBrowserRouter([
  {
    path:'/',  
    element:<App/>,    
    errorElement:<ErrorPage/>,
    children :
      [
        {index:true,element:<Home/>},
        {path:'/home',  element:<Home/>},
        {path:'/products',  element:<Product/>},
        {path:'/products/:id',  element:<ProductDetails/>},
        {path:'/contact',  element:<Contact/>},
      ]
},
  
  
])


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <RouterProvider router={routes}/>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
