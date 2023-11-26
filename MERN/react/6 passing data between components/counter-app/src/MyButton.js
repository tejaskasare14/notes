function MyButton(props)
{
  const increamentCounter = () => props.onIncrement(props.increantBy)
  return <button onClick={increamentCounter}>+ {props.increantBy}</button>
}

export default MyButton