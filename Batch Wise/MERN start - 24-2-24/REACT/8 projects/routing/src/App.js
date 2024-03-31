import logo from './logo.svg';
import './App.css';
import Navbar from './components/navabr/Navbar';
import { Outlet } from 'react-router-dom';

function App() {
  return (
    <>
      <Navbar/>
      <Outlet/>
    </>
  );
}

export default App;
