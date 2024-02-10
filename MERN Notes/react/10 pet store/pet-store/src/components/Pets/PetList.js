import { useState } from "react"
import { useFetchApi } from "../../hooks/useFetchApi"
import Navbar from "../Navbar"
import Form from "../Form"
import FormValidationUsingRHF from "../FormValidationUsingRHF"



let original_products = []
export function PetList() {
  
   let [url, setUrl] = useState("http://localhost:3000/pets")
   //fetching data from our custom hook
   let { data: products, isLoading } = useFetchApi(url)

   const filterPets = (pet_type) =>
   {
      //() => setUrl(`http://localhost:3000/pets?pet_type=${pet_type}`)
      setUrl(`http://localhost:3000/pets?pet_type=${pet_type}`)
      console.log(url);
   }

   return (
      <>
         <Navbar onFilter={filterPets}/>
         {/* <Form/> */}
         <FormValidationUsingRHF/>
         
      </>
   )
}

