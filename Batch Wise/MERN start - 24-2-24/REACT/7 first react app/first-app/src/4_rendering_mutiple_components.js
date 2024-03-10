import React from 'react';
import ReactDOM from 'react-dom/client';

function Button()
{
   return <button>Click me</button>
}

function Display()
{
   const my_name = "Tejas"
  return <h1>Hello {my_name} </h1>
}
const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render([<Button/>,<Display/>]);

// root.render( <div> <Button/> <Display/> </div> );

// root.render(<React.Fragment> <Button/> <Display/> </React.Fragment>);

root.render(
   <>
      <Button/>,<Display/>
   </>
);


