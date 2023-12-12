import { useCallback, useEffect, useState } from "react"
import { Products } from "./Products"
import { useFetchApi } from "../../hooks/useFetchApi"



let original_products = []
export function ProductList() {

   // let [products,setProducts] = useState([])  
   let [url, setUrl] = useState("http://localhost:3000/products")

   //fetching data without async await patter
   // useEffect(()=>{
   //    fetch(url)
   //    .then(response => response.json())
   //    .then(data =>
   //       {
   //          original_products=data
   //          setProducts(data)
   //       })
   // },[url])

   //fetching data using async await pattern
   // const fetchProducts =async()=>
   // {
   //    let response=await fetch(url)
   //    let data=await response.json()
   //    original_products=data
   //    setProducts(data)
   // }

   // useEffect(()=>{
   //    fetchProducts()
   // },[url])

   //fetching data using async await and useCallback hook
   // const fetchProducts =useCallback(async()=>  //useCallback work with function reference based on its dependncy
   // {
   //    let response=await fetch(url)
   //    let data=await response.json()
   //    original_products=data
   //    setProducts(data)
   // },[url])

   // useEffect(()=>{
   //    fetchProducts()
   // },[fetchProducts])

   //fetching data from our custom hook

   let { data: products, isLoading } = useFetchApi(url)


   return (
      <>

         {/* without bootstrap  */}
         {/* <p>ProductList</p>                                                          
               {
                  products.map(product => {
                     return (
                           <Products {...product} key={product.id}/>
                     )
                  })
               } */}

         <div className="container">
            <div className="btn-group" role="group" aria-label="Basic radio toggle button group">
               <input type="radio" className="btn-check" name="btnradio" id="btnradio1" onClick={() => setUrl("http://localhost:3000/products")} />
               <label className="btn btn-outline-primary" htmlFor="btnradio1">All</label>

               <button onClick={() => setUrl("http://localhost:3000/products")}>All</button>

               <input type="radio" className="btn-check" name="btnradio" id="btnradio2" onClick={() => setUrl("http://localhost:3000/products?category=mobile")} />
               <label className="btn btn-outline-primary" htmlFor="btnradio2">Mobile</label>

               <input type="radio" className="btn-check" name="btnradio" id="btnradio3" onClick={() => setUrl("http://localhost:3000/products?category=tv")} />
               <label className="btn btn-outline-primary" htmlFor="btnradio3">TV</label>

               <input type="radio" className="btn-check" name="btnradio" id="btnradio4" onClick={() => setUrl("http://localhost:3000/products?category=fridge")} />
               <label className="btn btn-outline-primary" htmlFor="btnradio4">Fridge</label>

               <input type="radio" className="btn-check" name="btnradio" id="btnradio5" onClick={() => setUrl("http://localhost:3000/products?category=ac")} />
               <label className="btn btn-outline-primary" htmlFor="btnradio5">Ac</label>
            </div>
            <div>
               {isLoading ? "Loading..." :
                  <div className="row">
                     {
                        products && products.length > 0 ? products && products.map(product => {
                           return (
                              <Products {...product} key={product.id} />
                           )
                        }) : <p>No products with this category</p>

                     }
                  </div>}
            </div>

         </div>
      </>
   )
}
