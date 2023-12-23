import React, { useState } from 'react'
export default function Form() {
  let [formData,setFormData]=useState({
    name:'',
    email:''
  })
   const captureForm=(event)=>
   {
      // setFormData(event.target.value)
      setFormData({
        ...formData,
        [event.target.name]:event.target.value
      })
   }
   const submitForm = (event) =>
   {
      event.preventDefault();
      console.log(formData);
   }
  return (
    <div>
      <form onSubmit={submitForm}>
         <label htmlFor="username">Name:</label>
         <input type="text" id="username" value={formData.name} name="name" onChange={captureForm}/>

         <br /><br />

         <label htmlFor="useremail">Email:</label>
         <input type="text" id="useremail" value={formData.email} name="email" onChange={captureForm}/>

         <input type="submit" />

         <p>Data {JSON.stringify(formData)}</p>
         
      </form>
    </div>
  )
}
