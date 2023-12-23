import React, { useState } from 'react'
export default function Form() {
  let [formData,setFormData]=useState({
    username:'',
    useremail:'',
    usercourse:'java'
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
         <input type="text" id="username" value={formData.username} name="username" onChange={captureForm}/> <br /><br />

         <label htmlFor="useremail">Email:</label>
         <input type="text" id="useremail" value={formData.useremail} name="useremail" onChange={captureForm}/> <br /><br />

         <label htmlFor="usercourse">Course:</label>
         <select id="usercourse" value={formData.usercourse} name="usercourse" onChange={captureForm}>
            <option value="dse">Data Software Enginnering</option>
            <option value="java">Java</option>
            <option value="python">Python</option>
            <option value="ds">Data Science</option>
          </select> <br /><br />
         
         <input type="submit" />

         <p>Data {JSON.stringify(formData)}</p>
         
      </form>
    </div>
  )
}
