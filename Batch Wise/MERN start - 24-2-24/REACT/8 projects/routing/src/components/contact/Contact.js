import React, { useState } from 'react'

export default function Contact() {
  const [contactForm,setContactForm]=useState({
    username:'',
    useremail:'',
    useraddress:'',
    usercountry:'',
    usergender:'',
    useragreement:false,
  })
  const [errors,setErrors]=useState({})

  const handleSubmit = (event)=>{
      event.preventDefault()
      if(contactForm.username==='' || contactForm.username===null)
      {
        setErrors({name:'Please enter your name'})
        return
      }
      setErrors({})
        console.log(contactForm);
  }

  const handleChange = (event)=>{
    // console.log(event);
    // console.log(event.target.value);
    // console.log(event.target.type);
    // console.log(event.target.name);


    setContactForm(
      {
        ...contactForm,
        // [event.target.name]:event.target.value
        [event.target.name]:event.target.type=='checkbox'?event.target.checked : event.target.value
      }
    )
}
  return (
    <div>
      <h1 style={{color:"red",textAlign:"center"}}>Contact US</h1>
      <form onSubmit={handleSubmit} style={{textAlign:'center'}} noValidate>
          <label htmlFor="username">UserName: </label>
          <input type="text" id='username' 
                              name='username' 
                              value={contactForm.username}
                              onChange={handleChange} formNoValidate
                                  />
          <br />
          {errors && errors.name && errors.name}
          <br/><br/>
          <label htmlFor="useremail">UserEmail: </label>
          <input type="email" id='useremail' 
                              name='useremail' 
                              value={contactForm.useremail}
                              onChange={handleChange} formNoValidate/>
          <br/><br/>
          <label htmlFor="useraddress">Address: </label>
          <textarea id="useraddress" cols="20" rows="5"
                              name='useraddress' 
                              value={contactForm.useraddress}
                              onChange={handleChange} formNoValidate></textarea>
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

          <label>User Gender: </label>
          <input type="radio" id='usergender1' name='usergender' value='male'onChange={handleChange} />
          <label htmlFor="usergender1">Male</label>

          <input type="radio" id='usergender2' name='usergender' value='female'onChange={handleChange} />
          <label htmlFor="usergender2">Female</label>
          <br/><br/>

          <input type="checkbox" id='useragreement' name='useragreement' value={contactForm.useragreement}
            onChange={handleChange} />
          <label htmlFor="useragreement">Accespt terms and conditions</label>
          <br/><br/>

          <input type="submit" style={{width:"100vh"}}/>
      </form>
    </div>
  )
}
