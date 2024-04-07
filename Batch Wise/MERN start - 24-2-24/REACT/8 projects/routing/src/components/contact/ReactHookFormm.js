import React from 'react'
import { useForm } from 'react-hook-form'

export default function ReactHookFormm() {
   const {register,handleSubmit,formState}=useForm()
   //to register out input tag use register
   //handlesubmit check the validation before submitting data
   //formState manage the errors
   const submitData =(data) =>{
      console.log(data);
   }

  return (
    <div>
      <form onSubmit={handleSubmit(submitData)}>
      <label>First Name</label>
      <input type='text' {...register("firstname",{required:true,minLength:3})} />
      <br />
      {formState.errors && formState.errors.firstname && formState.errors.firstname.type=="required" && "First name is required"}
      
      {formState.errors && formState.errors.firstname && formState.errors.firstname.type=="minLength" && "min 3 characters required"}
  
         <br /><br />
      <label>Last Name</label>
      <input type='text' {...register("lastname")} />
         <br /><br />
      <input type="submit" />
    </form>
    </div>
  )
}
