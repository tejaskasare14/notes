
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import Filter from './components/product/Filter';
import Search from './components/product/Search';
import ProductList from './components/product/ProductList';
import { useEffect, useState } from 'react';
import useFetchApi from './hooks/useFetchApi';

function App() { 
  let [url, setsetUrl]=useState("http://localhost:3000/products")
  let {data:products,loading,setData,error}=useFetchApi(url)

  const changeUrl =(category) =>{
      setsetUrl("http://localhost:3000/products?category="+category)
  }

  //searching logic
const searchProduct = (productName) =>
{

    let searchedProducts = products.filter(product => 
                                            product.name.toLowerCase()
                                            .includes(productName.toLowerCase())
                                          )
    // setProducts(searchedProducts) 
    setData(searchedProducts)
}
  

  return (
    <>
     <div className='container'>
        <div className="row">
            <div className="col-lg-6 p-2 text-center">
              <Filter onChageUrl={changeUrl}/>
            </div>
            <div className="col-lg-6 p-2">
              <Search onSearch={searchProduct}/>
            </div>
        </div>
        <div className="row mt-3">
            <div className="col text-center">
            {loading && <img src="https://cdn.pixabay.com/animation/2023/10/08/03/19/03-19-26-213_512.gif" alt=""/>}
            {error && <img src="https://t4.ftcdn.net/jpg/05/24/04/51/360_F_524045110_UXnCx4GEDapddDi5tdlY96s4g0MxHRvt.jpg" alt=""/>}
            </div>
        </div>
       
        
        <div className="row mt-3">
            <div className="col">
              <ProductList products={products} />
            </div>
        </div>
     </div>
    </>
  );
}

export default App;
