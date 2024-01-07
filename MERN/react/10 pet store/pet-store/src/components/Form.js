import React from 'react'
import { useState } from 'react'

export default function Form() {
   let [formData,setFormData]=useState({
     username:'',
     useremail:'',
   })
    const captureForm=(event)=>
    {
       // setFormData(event.target.value)
       setFormData({
         ...formData,
         [event.target.name]:event.target.value
       })
    }

    const [errors,setErrors ]=useState({})
    const submitForm = (event) =>
    {
      event.preventDefault();
      if(formData.username =="" || formData.username == null)
      {
         //alert("name is invalid")
         setErrors({name:"name is invalid"})
         return
      }
      else if(formData.useremail =="" || formData.useremail == null)
      {
         //alert("email is invalid")
         setErrors({email:"email is invalid"})
         return
      }
       console.log(formData);
       setErrors({})
 
    }



   return (
     <div>
       <form onSubmit={submitForm} noValidate>
          <label htmlFor="username">Name:</label>
          <input type="text" id="username" value={formData.username} name="username" onChange={captureForm} required formNoValidate/> <br /><br />
          {errors && errors.name && errors.name}


          <label htmlFor="useremail">Email:</label>
          <input type="text" id="useremail" value={formData.useremail} name="useremail" onChange={captureForm} formNoValidate/> <br /><br />
          {errors && errors.email && errors.email}

          <input type="submit" />
 
          <p>Data {JSON.stringify(formData)}</p>
          
       </form>
     </div>
   )
 }
