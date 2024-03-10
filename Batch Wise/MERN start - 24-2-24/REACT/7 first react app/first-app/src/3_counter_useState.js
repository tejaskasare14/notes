import { useState } from 'react';
import ReactDOM from 'react-dom/client';
function Button()
{ 
   let [counter,setCounter]=useState(0)

   const updateCounter = ()=>{
                                 setCounter(counter+1)
                             }
   return <div>
            <p>Counter is : {counter}</p>
            <button onClick={updateCounter}>+1</button>
         </div>
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Button/>);