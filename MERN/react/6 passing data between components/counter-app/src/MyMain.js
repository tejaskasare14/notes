import MyButton from "./MyButton"
import MyCounter from "./MyCounter"
import React, { useState } from 'react';

function MyMain()
{
  let [count,updateCount] = useState(0)
  const incCounter = (value) => {updateCount(count+=value)}
  return <>
  <MyCounter countervalue={count}/> {/*For Counter componet, value of count goes as a property named countervalue */}
  <MyButton onIncrement={incCounter} increantBy={1}/>
  <MyButton onIncrement={incCounter} increantBy={5}/>
  <MyButton onIncrement={incCounter} increantBy={10}/>
  <MyButton onIncrement={incCounter} increantBy={100}/>
  </>
}

export default MyMain