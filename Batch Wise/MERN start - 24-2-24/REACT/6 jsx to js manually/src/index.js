function MyComponent()
      {
         return <h1>This h1 is created in JSX</h1>;
      }

let root = document.getElementById("root")

let reactRoot=ReactDOM.createRoot(root)
reactRoot.render( <MyComponent/> ) 
