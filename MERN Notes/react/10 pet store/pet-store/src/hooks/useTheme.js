import { useContext, useState } from "react"
import { ThemeContext } from "../context/ThemeProvider"

export const useTheme = () =>
{
   const context=useContext(ThemeContext)
   return context
}