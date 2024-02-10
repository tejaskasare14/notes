function Myh1Component ()
      {
         return <h1>Hello React</h1>;  
      }

      let root = document.getElementById("root")

      let div_container = ReactDOM.createRoot(root)
      div_container.render(
         <Myh1Component/> 
      )