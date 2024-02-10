import { useEffect, useState } from "react"
import CardList from "./CardList"
import SearchEmployee from "./SearchEmployee"
// import employee from './emp-data.json'


let original_employees =[]
function App()
{
   let [employees,setEmployees]=useState([])

   //api call without useEffect -> infinite api call
   // fetch("http://localhost:3000/emp-data.json")
   //    .then(response => response.json())
   //    .then(data=>setEmployees(data))
   //    .catch()


   //api call with useEffect -> without any dependency
   // useEffect(()=> { 
   //                   fetch("http://localhost:3000/emp-data.json")
   //                   .then(response => response.json())
   //                   .then(data=>
   //                         {
   //                            original_employees = data
   //                            setEmployees(data)
   //                         })
   //                },[])

   //api call with useEffect -> with  dependency
   let [api_call_counter, setApiCall] = useState(1)
   useEffect(()=> { 
      fetch("http://localhost:3000/emp-data.json")
      .then(response => response.json())
      .then(data=>
            {
               original_employees = data
               setEmployees(data)
            })
   },[api_call_counter])

   const please_call_api =() => {setApiCall(api_call_counter+1)}

   const filterEmployees = (emp_name) =>
   {
      setEmployees(original_employees.filter(emp => 
      {
         return emp.name.toLowerCase().includes(emp_name.toLowerCase())
      }))
   }
   return(
      <>
         <button onClick={please_call_api}>{api_call_counter}</button>
         <SearchEmployee onSearch={filterEmployees}/>
         <CardList employees={[...employees]}/>
      </>
   )
}

export default App