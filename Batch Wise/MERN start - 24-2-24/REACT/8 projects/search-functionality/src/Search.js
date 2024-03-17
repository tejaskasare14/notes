import React, { useRef, useState } from 'react'
import './search.css'

// export default function Search() {
//   const productName=useRef()
//   const submitForm = (event) =>{
//     //event.preventDefault() used to prevent refreshing of page
//     event.preventDefault();
//     console.log(productName.current.value);
//   }
//   return (
//     <div>
//       <form onSubmit={submitForm}>
//         <input type="text" placeholder='Product Name' ref={productName}/>
//         <button>Search</button>
//       </form>
//     </div>
//   )
// }



export default function Search(props) {
  let [productName, setProductName]=useState('')
  
  const submitForm = (event) =>{
    event.preventDefault();
    console.log(productName);
    props.onSearch(productName)
  }

  const changeProductName =(event) => 
  {
    //console.log(event.target.value);
    setProductName(event.target.value)
    
  }
  return (
    <div>
      <form onSubmit={submitForm}>
        <input type="text" placeholder='Product Name' onChange={changeProductName}/>
        <button>Search</button>
      </form>
    </div>
  )
}
