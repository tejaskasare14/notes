import React from 'react'
import Card from './Card'

export default function CardList(props) 
{
    let products = props.products
    return (
        products.map(product =>
          {
            return <Card {...product} key={product.id}/>  
          })
    )
}
