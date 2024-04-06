import React from 'react'
import { useParams,useNavigate, useSearchParams } from 'react-router-dom';
import products from '../../products.json'

export default function ProductDetails() {
  const param=useParams() //to get id from url
  const [serach_param] = useSearchParams()
  console.log(serach_param.get('name'));

  const navigate=useNavigate()
  console.log(param.id);
  return (
    <div className='card'>
      {
      products.map((product) => 
                      {
                          if(product.id==param.id)
                          {
                            return(
                                <div className='card-items' style={{width:200}} key={product.id}>
                                  <img src={product.image} width="200px" height="200px"/>
                                  <h2>{product.title}</h2>
                                  <h4>Price : {product.price}</h4>
                                  <button onClick={()=>navigate('/product')}>Back</button>
                                </div>
                               )
                          }
                      })
      }

      
    </div> 
    
  )
}
