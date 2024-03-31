import React, { useEffect, useState } from 'react'

export default function useFetchApi(url) {
   let [data, setData]=useState(null)
   let [loading, setLoading]=useState(true)
   let [error, setError]=useState(null)

   //const  conteroller=new AbortController();
   const fetchProducts = async() =>
   {
      
      try 
      {
         let  response= await fetch(url)
         let result=await response.json()
         setLoading(false)
         setData(result)
      }
      catch(er)
      {
         setError(er)
         setLoading(false)
      }
      
     
   }
   useEffect(()=>
   {
     fetchProducts() ;
     //return () => {conteroller.abort();}
   },[url])

  
  return {data,loading,setData,error} 
}
