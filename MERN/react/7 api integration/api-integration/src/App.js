import { useState } from "react"
import CardList from "./CardList"
import SearchEmployee from "./SearchEmployee"
import employee from './emp-data.json'

function App()
{
   let [employees,setEmployees]=useState(employee)

   const filterEmployees = (emp_name) =>
   {
      setEmployees(employee.filter(emp => 
      {
         return emp.name.toLowerCase().includes(emp_name.toLowerCase())
      }))
   }
   return(
      <>
         <SearchEmployee onSearch={filterEmployees}/>
         <CardList employees={[...employees]}/>
      </>
   )
}

export default App