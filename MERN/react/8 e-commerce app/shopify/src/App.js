import logo from './logo.svg';
import './App.css';
import { ProductList } from './components/products/ProductList';
import Navbar from './components/Navbar';
import { Outlet } from 'react-router-dom';

function App() {
  return (
    <>
      <Navbar/>
    </>
  );
}

export default App;
