import React from 'react'

export default function ProductList(props) {
  return (
    <>
    <div className="row">
    {props.products && props.products.map(product => 
      <div className="col-lg-4 mb-3" key={product.id}>
              <div className="card text-center" style={{width: "18rem"}}>
                <div className="card-body">
                    <h5 className="card-title">{product.name}</h5>
                    <p className="card-text">Category : {product.category}</p>
                    <p className="card-text">Price : {product.price}</p>
                    <a href="#" className="btn btn-primary">Add to cart</a>
                </div>
              </div>
              </div>
            )}
    </div> 
    </>
  )
}
