import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import NotFound from './components/error page/NotFound';
import Home from './components/home/Home';
import Contact from './components/contact/Contact';
import Product from './components/product/Product';
import ProductDetails from './components/product/ProductDetails';
import ReactHookFormm from './components/contact/ReactHookFormm';

const routes=createBrowserRouter([
  {
    path:"/",
    element:<App/>,
    errorElement:<NotFound/>,
    children:[
      {
        index:true,
        element:<Home/>
      },
      {
        path:'/home',
        element:<Home/>
      },
      {
        path:'/contact',
        element:<ReactHookFormm/>
      },
      {
        path:'/product',
        element:<Product/>
      },
      {
        path:'/product/:id',
        element:<ProductDetails/>
      } 
    ]
  }
])

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  // <React.StrictMode>
  //   <App />
  // </React.StrictMode>
  <RouterProvider router={routes}/>
  
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
