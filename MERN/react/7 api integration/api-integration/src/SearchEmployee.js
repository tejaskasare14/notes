import { useRef, useState } from "react";

function SearchEmployee(props)
{

   //collecting data from form way 1: using useRef
   //way 1 line 1
   //let employee_name = useRef()

   //collecting data from form way 2: using useState
   //way 2 line 1
   let [employee_name,setEmployeeName] = useState('')

   //way 2 line 3
   const changeEmpName =(event) => 
   {
      //console.log(employee_name);
      setEmployeeName(event.target.value)   
   }

   const employee_search=(event)=>
   {
      // console.log(event);
       //way 1 line 3
      //console.log(employee_name);
       //way 1 line 4
      //console.log(employee_name.current.value);

         console.log(employee_name);
         props.onSearch(employee_name)
      event.preventDefault()
   }

   return (
      <>
      <form onSubmit={employee_search}>
         {/* way 1 line 2 */}
         {/* <input type="text" ref={employee_name}/> */}

         {/* way 2 line 2 */}
         <input type="text" value={employee_name} onChange={changeEmpName}/>

         <button>Search</button>
      </form>
      </>
   )
}

export default SearchEmployee