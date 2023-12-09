

export function Products(props)
{
   let product  = props
   return(
         <div>
            <ul>
               <li>
                  <h1>Name : {product.name}</h1>
                  <h3>Category : {product.category}</h3>
                  <p>Description : {product.description}</p>
               </li>
            </ul>
         </div>
   )
}