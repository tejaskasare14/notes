import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from './reportWebVitals';
import MyMain from './MyMain';

//need of useState
function Counter1()
{
    let count = 0

    let incCounter = ()=>{
      count = count+1
      console.log(count);
    }

    return <div>
        <p>Counter = {count}</p> 
        <button onClick={incCounter}>click here to increment counter {count}</button>
    </div> 
    ;
}

//use of useState
function Counter2()
{
  //let count = 0
  let [count, updateCounter]=useState(0)
    let incCounter = ()=>{
      updateCounter(count+1)
    }

    return <div>
        <p>Hello React</p>
        <p>Counter = {count}</p> 
        <button onClick={incCounter}>click here to increment counter {count}</button>
    </div> 
    ;
}
//const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <Counter2/>
// );

// rendering mutiple component at a time
function Component1()
  {
    return <h1>Hello From compoent 1</h1>
  }
function Component2()
  {
    return <h1>Hello From compoent 2</h1>
  }
//const root = ReactDOM.createRoot(document.getElementById('root'));
/*root.render(
  //way 1 of redenring mutiple component
  //[<Component1/>, <Component2/>]

  //way 2 of redenring mutiple component
  // <div>
  //   <Component1/>
  //   <Component2/>
  // </div>

  //way 3 of redenring mutiple component
  // <React.Fragment>
  //   <Component1/>
  //   <Component2/>
  // </React.Fragment>

  //way 4 of redenring mutiple component
  <>
    <Component1/>
    <Component2/>
  </>
);*/

//returning mutiple components from one componeent
function Child1()
  {
    return <h1>Hello from child 1</h1>
  }

function Child2()
  {
    return <h1>Hello from child 2</h1>
  }

function Parent()
  {
    return <>
    <h1>Hello This is parent componet</h1>
    <Child1/>
    <Child2/>
    </>
  }
// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//  <Parent/>
// );

//passing data between compoents
function Button(props)
{
  const increamentCounter = () => props.onIncrement()
  return <button onClick={increamentCounter}>Click me to increment counter</button>
}

function Counter(props)
{
  return <p>Counter = {props.countervalue}</p>
}

function Main()
{
  let [count,updateCount] = useState(0)
  const incCounter = () => {updateCount(count+=1)}
  return <>
  <Counter countervalue={count}/> {/*For Counter componet, value of count goes as a property named countervalue */}
  <Button onIncrement={incCounter}/>
  </>
}
// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//  <Main/>
// );

//passing function between component with arguments
function Button11(props)
{
  const increamentCounter = () => props.onIncrement(props.increantBy)
  return <button onClick={increamentCounter}>+ {props.increantBy}</button>
}

function Counter22(props)
{
  return <p>Counter = {props.countervalue}</p>
}

function Main11()
{
  let [count,updateCount] = useState(0)
  const incCounter = (value) => {updateCount(count+=value)}
  return <>
  <Counter22 countervalue={count}/> {/*For Counter componet, value of count goes as a property named countervalue */}
  <Button11 onIncrement={incCounter} increantBy={1}/>
  <Button11 onIncrement={incCounter} increantBy={5}/>
  <Button11 onIncrement={incCounter} increantBy={10}/>
  <Button11 onIncrement={incCounter} increantBy={100}/>
  </>
}
// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//  <Main11/>
// );

//making saparate file for each compoent
//create 3 files in src folder - MyButton.js, MyCounter.js, MyMain.js and add given code
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
 <MyMain/>
);



// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
