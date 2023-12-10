

export function Products(props)
{
   let product  = props
   return(
      //without botstra card
      // <div>
      //    <ul>
      //          <li>
      //             <h1>Name : {product.name}</h1>
      //             <h3>Category : {product.category}</h3>
      //             <p>Description : {product.description}</p>
      //          </li>
      //       </ul>
      // </div>
                <div className="col-lg-3 mb-3">
                     <div className="card" style={{width: "15rem"}} >
                        <img src={product.image} className="card-img-top" alt="..." style={{height:"200px"}}/>
                        <div className="card-body">
                           <h5 className="card-title">{product.name}</h5>
                           <p className="card-text">Description : {product.description}</p>
                           <p className="card-text">Category : {product.category}</p>
                           <a href="#" className="btn btn-primary">Go somewhere</a>
                        </div>
                     </div>
               </div>
   )
}