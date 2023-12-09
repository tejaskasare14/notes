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
         <p>ProductList</p>                                                        u7fv vcv cvdc
            {
               products.map(product => {
                  return (<Products {...product} key={product.id}/>)
               })
               
            }
      </>
   )
}
