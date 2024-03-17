import { useState } from "react"
import Display from "./Display"
import Button from "./Button"


function App()
{
   let [counter,setCounter]=useState(0)

   const updateCounter = (value)=>{
                                 setCounter(counter+value)
                             }
   return <>
      <Display data={counter}/>
      <Button function_call={updateCounter} buttonValue={1}/>
      <Button function_call={updateCounter} buttonValue={5}/>
      <Button function_call={updateCounter} buttonValue={10}/>
   </>
}

export default App