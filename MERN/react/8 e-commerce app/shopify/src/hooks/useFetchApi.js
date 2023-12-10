import { useState,useEffect } from "react"


export const useFetchApi=(url)=>
{
   let [data,setData]=useState(null)
   let [isLoading,setLoading]=useState(false)

   useEffect(()=>{
            const fetchData =(async()=> 
               {
                  setLoading(true)
                  setData(null)

                  let response=await fetch(url)
                  let record=await response.json()
                  console.log(record);
                  
                  setData(record)
                  setLoading(false)
               })
               fetchData()
   },[url])

   return {data,isLoading}

}

