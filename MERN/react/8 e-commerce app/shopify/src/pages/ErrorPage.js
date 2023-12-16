import { useRouteError } from "react-router-dom"

export default function ErrorPage() {
   const error = useRouteError()
  return (
    <div>
      <img src="https://sitechecker.pro/wp-content/uploads/2023/06/404-status-code.png" alt="" height={300+'px'}/>
      <h1>Page Not Found</h1>
      <p>{error.status} - {error.statusText}</p>
    </div>
  )
}
