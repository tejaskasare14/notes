import React, { useState } from 'react'
export default function Form() {
  let [formData,setFormData]=useState({
    username:'',
    useremail:'',
    usercourse:'java',
    usergender:'',
    useragreement:false
  })
   const captureForm=(event)=>
   {
      // setFormData(event.target.value)
      setFormData({
        ...formData,
        [event.target.name]:event.target.type ==="checkbox"?event.target.checked:event.target.value
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

          <label htmlFor="usergender">Gender:</label>
          <input type="radio" id="usergender" value='m' name="usergender" onChange={captureForm}/>Male
          <input type="radio" id="usergender" value='f' name="usergender" onChange={captureForm}/>Female <br /><br />

          <input type="checkbox" id="useragreement" checked={formData.useragreement} name="useragreement" onChange={captureForm}/>
          Agree terms and conditions
          

         
         <input type="submit" />

         <p>Data {JSON.stringify(formData)}</p>
         
      </form>
    </div>
  )
}
