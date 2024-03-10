import ReactDOM from 'react-dom/client';
const root1 = document.getElementById('root1');
const root2 = ReactDOM.createRoot(document.getElementById('root2'));

setInterval(() => {
   //actal DOM
   root1.innerHTML = `<div>
                           <h1>This is actual dom</h1>
                           <input type="text" />
                           <h1>${new Date().toLocaleTimeString()}</h1>
                        </div>`;

   //virtual DOM
   root2.render(       <div>
                           <h1>This is virual dom</h1>
                           <input type="text" />
                           <h1>{new Date().toLocaleTimeString()}</h1>
                        </div>);
}, 1000);

