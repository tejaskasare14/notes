import React from 'react'
import { useSelector } from 'react-redux'
import { selectCount } from '../slices/counterSlice'

export default function GetCounter() {
  const count=useSelector(selectCount)
  return (
    <div>
      <h1>GetCounter component</h1>
      <h3>{count}</h3>
    </div>
  )
}
