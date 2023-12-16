import { useState,useEffect } from "react"


export const useFetchApi=(url)=>
{
   let [data,setData]=useState(null)
   let [isLoading,setLoading]=useState(false)

   useEffect(()=>{
           
            const fetchData =async()=> 
               {
                  setLoading(true)
                  setData(null)

                  let response=await fetch(url)
                  //handling error
                        // console.log(response)
                        // console.log(response.ok);
                        // if(!response.ok)
                        // {
                        //    console.log(`OOPS ! Error occur,${response.status} ${response.statusText}`);
                        // }
                  //handling error
                  let record=await response.json()
                  console.log(record);
                  
                  setData(record)
                  setLoading(false)
               }
               fetchData();

           
   },[url])

   return {data,isLoading}

}

