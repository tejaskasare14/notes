import React from 'react'
import products from '../../products.json'
import './card.css'
import { Link } from 'react-router-dom'

export default function Product() {
  return (
  <div className='card'>
    {  
        products.map(product =>
          {
            return (
                <div className='card-items'>
                    <img src={product.image} width="200px" height="200px"/>
                    <h2>{product.title}</h2>
                    <h4>Price : {product.price}</h4>
                    <button><Link to={`/product/${product.id}`}>View More</Link></button>
                  </div>
              
              ) 
          })
      }
  </div>
  )
}
