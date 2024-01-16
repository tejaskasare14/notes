import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { decrementByOne, incrementByN, incrementByOne, selectCount } from '../slices/counterSlice'

export default function ChangeCounter() {
  const dispatch=useDispatch()
  const count=useSelector(selectCount)
  return (
    <div>
      <button onClick={()=>dispatch(incrementByOne())}> +1 </button> {count} <button onClick={()=>dispatch(decrementByOne())}> -1 </button> <br /><br />
      <button onClick={()=>dispatch(incrementByOne())}> +1 </button> {count} <button onClick={()=>dispatch(incrementByN(5))}> +n </button> <span>you  can provide nay number instead of n</span>
      
    </div>
  )
}
