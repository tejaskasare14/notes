import ReactDOM from 'react-dom/client';

function Display()
{
  let my_name = "tejas"
  return <h1>Hello {my_name} welcome to my first React App</h1>
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Display/>);

