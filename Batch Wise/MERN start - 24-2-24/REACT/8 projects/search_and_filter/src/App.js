
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import Filter from './components/product/Filter';
import Search from './components/product/Search';
import ProductList from './components/product/ProductList';
import { useState } from 'react';
import { useEffect } from 'react';

function App() { 
  let [products, setProducts]=useState([])
  let [url, setsetUrl]=useState("http://localhost:3000/products")
  console.log(products);

  useEffect(()=>{
      fetch(url)
      .then(res => res.json()
                        // .then(data=>console.log(data))
                        .then(data=>setProducts(data))
                        .catch())
      .catch()
  },[url])

  const changeUrl =(category) =>{
      setsetUrl("http://localhost:3000/products?category="+category)
  }

  return (
    <>
     <div className='container'>
        <div className="row">
            <div className="col-lg-6 p-2 text-center">
              <Filter onChageUrl={changeUrl}/>
            </div>
            <div className="col-lg-6 bg-primary">
              <Search/>
            </div>
        </div>
        <div className="row mt-3">
            <div className="col">
              <ProductList products={products}/>
            </div>
        </div>
     </div>
    </>
  );
}

export default App;
