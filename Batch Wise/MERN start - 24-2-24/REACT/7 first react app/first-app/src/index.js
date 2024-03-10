import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';

function Button(props)
{
   return <button onClick={props.function_call}>Click me</button>
}

function Display(props)
{
   const counter_value = props.data
  return <h1>Counter is :  {counter_value} </h1>
}

function App()
{
   let [counter,setCounter]=useState(0)

   const updateCounter = ()=>{
                                 setCounter(counter+1)
                             }
   return <>
      <Display data={counter}/>
      <Button function_call={updateCounter}/>
   </>
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App/>);


