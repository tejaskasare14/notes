import { useState } from "react"
import Card from "./Card"
import employee from './emp-data.json'

function CardList()
{
   // let page_no = 0
   let [page_no, setPageNumber] = useState(0)
   let per_page = 3
   let start_index = 0
   let end_index = 3
   // let employees = employee.slice(start_index,end_index)
   let [employees,setEmployees]=useState(employee.slice(start_index,end_index))

   let previous_page = () =>{
        
         if(page_no>0)
         {
            setPageNumber(page_no-=1)
            start_index = page_no * per_page
            end_index = start_index + per_page
            console.log(start_index,end_index);
            setEmployees(employee.slice(start_index,end_index))
         }     
   }

   let next_page = () =>{
      
      if(page_no<(Math.floor(employee.length/per_page)))
      {
         setPageNumber(page_no+=1)
         start_index = page_no * per_page
         end_index = start_index + per_page
         console.log(start_index,end_index);
         setEmployees(employee.slice(start_index,end_index))
      }     
}
   return(
      <>
         <p>Current Page {page_no+1}</p>
         <button onClick={previous_page} disabled={page_no==0 || page_no<0?true:false}>Previous </button>
         <button onClick={next_page}>Next </button>
         {/* sending data to card using array index */}
         {/* 
         <Card employee_data={employee[0]}/>
         <Card employee_data={employee[1]}/> */}
         
         {/* sending data to card using spread operator */}
         {/* <Card {...employee[0]}/> */}

         {/* display multiple cards */}
         {
            employees.map((employee) => 
               {
                  return <Card {...employee} key={employee.id}/>
               })
         }
        
      </>
   )
}

export default CardList