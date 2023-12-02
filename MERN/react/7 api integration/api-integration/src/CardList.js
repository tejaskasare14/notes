import Card from "./Card"
import employee from './emp-data.json'
function CardList()
{
   let page_no = 0
   let per_page = 3
   let start_index = 0
   let end_index = 3
   let employees = employee.slice(start_index,end_index)

   let pre_page = () =>{
         page_no-=1
         if(page_no>=0)
         {
            start_index = page_no * per_page
            end_index = start_index + per_page
            console.log(start_index,end_index);
            employee = employee.slice(start_index,end_index)
         }
         
   }
   return(
      <>
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
         <button onClick={pre_page}>Previous</button>
         <button>Next</button>
      </>
   )
}

export default CardList