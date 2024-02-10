import { useParams } from "react-router-dom"
import { useFetchApi } from "../../hooks/useFetchApi"
import { useEffect, useState } from "react"


export default function ProductDetails() {
   const param = useParams()

   let { data:product, isLoading } = useFetchApi(`http://localhost:3000/products/${param.id}`)
   console.log(param)
   console.log(param.id)
   console.log(product);
   if(product)
   {
      return (
         <div className="col-lg-3 mb-3">
         <div className="card" style={{width: "15rem"}} >
            <img src={product.image} className="card-img-top" alt="..." style={{height:"200px"}}/>
            <div className="card-body">
               <h5 className="card-title">{product.name}</h5>
               <p className="card-text">Description : {product.description}</p>
               <p className="card-text">Category : {product.category}</p>
            </div>
         </div>
   </div>
      )
   }
   


      
   
  
}
