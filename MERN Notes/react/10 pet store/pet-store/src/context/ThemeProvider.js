import React, { createContext, useReducer, useState } from 'react'

// using context
// export const ThemeContext  = createContext()

// export default function ThemeProvider(props) {

//   const [theme, setTheme]=useState('light')
//   return (
//     <ThemeContext.Provider value={{theme,setTheme}}>
//          {props.children}
//     </ThemeContext.Provider>
//   )
// }

// using reducer
export const ThemeContext  = createContext()
const themeReducer = (state,action)=>
{
  switch(action.type)
  {
    case 'CHANGE THEME':
      return{
        ...state,
        theme:action.payload
      }
    default:
      return state
  }
}
export default function ThemeProvider(props) {

  const [state,dispatch]=useReducer(themeReducer,{theme:'light'})
  //instead of dispatch you can write setState or updateStae

  const changeTheme = (themevalue) =>
  {
    dispatch({type:'CHANGE THEME',payload:themevalue})
  }
  return (
    <ThemeContext.Provider value={{...state,changeTheme}}>
         {props.children}
    </ThemeContext.Provider>
  )
}
