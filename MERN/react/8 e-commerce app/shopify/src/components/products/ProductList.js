import { useEffect, useState } from "react"
import { Products } from "./Products"


let original_products = []
export function ProductList()
{

   let [products,setProducts] = useState([])  
   
   useEffect(()=>{
      fetch("http://localhost:3000/products")
      .then(response => response.json())
      .then(data =>
         {
            original_products=data
            setProducts(data)
         })
   },[])

   return(
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
         <p>ProductList</p>
         <div className="container">
            <div className="row">                                                          
               {
                  products.map(product => {
                     return (
                           <Products {...product} key={product.id}/>
                     )
                  })
               }

            </div>
         </div>
      </>
   )
}
