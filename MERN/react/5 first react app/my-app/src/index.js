import React from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from './reportWebVitals';

function Myh1Component ()
      {
        let username = "Tejas"
         return <h1>Hello {username}</h1>; 
      }

const my_root = document.getElementById('root')
const root = ReactDOM.createRoot(my_root);
root.render(
  <Myh1Component/>
);

// diff between actual vs virtual dom by react
let div1 = document.getElementById('root1')
const div2 = document.getElementById('root2')
const my_root2 = ReactDOM.createRoot(div2);

setInterval(() => {

div1.innerHTML =`
  <div>
    <h1>Hello Actual DOM </h1>
    <input></input>
    <p>${new Date().toLocaleTimeString()}</p>
  </div>
`
my_root2.render(
 <div>
    <h1>Hello Virtual DOM</h1>
    <input></input>
    <p>{new Date().toLocaleTimeString()}</p>
 </div>
);
}, 1000);

// handling click jsx
function generateRandomNumber()
{
  console.log(Math.random());
}
function ButtonHandle ()
      {
         return <button onClick={generateRandomNumber}>click me</button>; 
      }

root.render(
  <ButtonHandle/>
);




// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
