import React, { useState } from 'react'

export default function Contact() {
  const [contactForm,setContactForm]=useState({
    username:'',
    useremail:'',
    useraddress:'',
    usercountry:''
  })
  const handleSubmit = (event)=>{
      event.preventDefault()
      console.log(contactForm);
  }

  const handleChange = (event)=>{
    //console.log(event.target.value);
    // console.log(event.target.name);
    setContactForm(
      {
        ...contactForm,
        [event.target.name]:event.target.value
      }
    )
}
  return (
    <div>
      <h1 style={{color:"red",textAlign:"center"}}>Contact US</h1>
      <form onSubmit={handleSubmit} style={{textAlign:'center'}}>
          <label htmlFor="username">UserName: </label>
          <input type="text" id='username' 
                              name='username' 
                              value={contactForm.username}
                              onChange={handleChange}
                                  />
          <br/><br/>
          <label htmlFor="useremail">UserEmail: </label>
          <input type="email" id='useremail' 
                              name='useremail' 
                              value={contactForm.useremail}
                              onChange={handleChange}/>
          <br/><br/>
          <label htmlFor="useraddress">Address: </label>
          <textarea id="useraddress" cols="20" rows="5"
                              name='useraddress' 
                              value={contactForm.useraddress}
                              onChange={handleChange}></textarea>
          <br/><br/>
          <label htmlFor="usercountry">Usercountry:</label>
          <select name="usercountry" id="usercountry" 
                      value={contactForm.usercountry}
                      onChange={handleChange}>
            <option value="india">INDIA</option>
            <option value="us">AMERICA</option>
            <option value="china">CHINA</option>
          </select>
          <br/><br/>
          <input type="submit" style={{width:"100vh"}}/>
      </form>
    </div>
  )
}
