function Button(props)
{
   
   const call_updateCounter = () => {
                                       props.function_call(props.buttonValue) 
                                    }
   return <button onClick={call_updateCounter}>+{props.buttonValue}</button>
}

export default Button