import React, { useContext } from 'react'
import { appendErrors, useForm } from 'react-hook-form';
import { ThemeContext } from '../context/ThemeProvider';
import { useTheme } from '../hooks/useTheme';
import sun from '../sun.svg'
import moon from '../moon.svg'

export default function FormValidationUsingRHF() {


      const {theme,setTheme}=useTheme()
      console.log(theme);

   let themeStyle = {}

   if(theme=='light')
   {
      themeStyle = {backgroundColor:'white',color:'black'}
   }
   else
   {
      themeStyle = {backgroundColor:'black',color:'white'}
   }

   const {register,handleSubmit,formState} = useForm()
   // register : to register a field with type of error 
   // handleSubmit : function to be called when we click on submit button 
   // formState : contains error information

   const submitForm = (data) => {
     // event.preventDefault(); NO need to write this. react hook form automatically handles prevent default
       console.log(data);
   }
   return (
      <div>
         <form onSubmit={handleSubmit(submitForm)} style={themeStyle}>
            <label htmlFor="username">Name:</label>
            <input type="text" id="username" {...register('name',{required:true,minLength:3,maxLength:10})}/> <br /><br />
            {formState.errors && formState.errors.name && formState.errors.name.type ==='required' && <span>Name is required</span> }
            {formState.errors && formState.errors.name && formState.errors.name.type ==='minLength' && <span>Min length for name is 3</span> }
            {formState.errors && formState.errors.name && formState.errors.name.type ==='maxLength' && <span>Max length for name is 10</span> }


            <label htmlFor="useremail">Email:</label>
            <input type="text" id="useremail" {...register('email')}/> <br /><br />

            <input type="submit" />

            {/* <p>Data {JSON.stringify(formData)}</p> */}

         </form>
         {
            theme=='light'? 
            <img src={moon} width={25} onClick={() => setTheme('dark')}/> : 
            <img src={sun} width={25} onClick={() => setTheme('light')}/>
         }
      </div>
   )
}
