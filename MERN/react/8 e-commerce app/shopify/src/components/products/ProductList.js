import { useEffect, useState } from "react"
import { Products } from "./Products"


let original_products = []
export function ProductList()
{

   let [products,setProducts] = useState([])  
   let [url, setUrl] = useState("http://localhost:3000/products")
   
   useEffect(()=>{
      fetch(url)
      .then(response => response.json())
      .then(data =>
         {
            original_products=data
            setProducts(data)
         })
   },[url])

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
        
         <div className="container">
               <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
                     <input type="radio" class="btn-check" name="btnradio" id="btnradio1" onClick={()=>setUrl("http://localhost:3000/products")}/>
                     <label class="btn btn-outline-primary" for="btnradio1">All</label>

                     <button onClick={()=>setUrl("http://localhost:3000/products")}>All</button>

                     <input type="radio" class="btn-check" name="btnradio" id="btnradio2"  onClick={()=>setUrl("http://localhost:3000/products?category=mobile")}/>
                     <label class="btn btn-outline-primary" for="btnradio2">Mobile</label>

                     <input type="radio" class="btn-check" name="btnradio" id="btnradio3" onClick={()=>setUrl("http://localhost:3000/products?category=tv")}/>
                     <label class="btn btn-outline-primary" for="btnradio3">TV</label>

                     <input type="radio" class="btn-check" name="btnradio" id="btnradio4" onClick={()=>setUrl("http://localhost:3000/products?category=fridge")}/>
                     <label class="btn btn-outline-primary" for="btnradio4">Fridge</label>
               </div>
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
