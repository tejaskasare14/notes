import React, { useState } from 'react'

export default function Search(props) {
  let [productName, setProdcutName] = useState('')

  const submitForm = (event) =>{ 
    event.preventDefault()
    props.onSearch(productName)
  }

  const changeProductName = (event)=>
  {
    setProdcutName(event.target.value)
  }
  return (
    <>
      <form className="row g-3" onSubmit={submitForm}>
        <div className="col-auto">
          <input type="text" className="form-control" id="product_name" placeholder="Product name" 
          onChange={changeProductName}/>
        </div>
        <div className="col-auto">
          <input type="submit" className="btn btn-primary mb-3"/>
        </div>
      </form>
    </>
  )
}
