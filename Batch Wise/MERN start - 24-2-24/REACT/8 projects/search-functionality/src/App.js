import './App.css';
import Search from './Search';
import CardList from './CardList';
import productsData from './products.json'
import './card.css'
import { useState } from 'react';

function App() {
  let [pageNo, setPageNo] = useState(0)
  let per_page = 3 
  let start = 0
  let end = 3
 
  let [products,setProducts]=useState(productsData.slice(start,end))

  function previousPage(){
    let prevpageNo = pageNo - 1
    setPageNo(prevpageNo)
    start = per_page * prevpageNo //0*1 = 3
    end = start+ per_page //3+3 = 6
    setProducts(productsData.slice(start,end))
  }
  const nextPage=() =>{
    let nextpageNo = pageNo + 1
    setPageNo(nextpageNo)
    start = per_page * nextpageNo //0*1 = 3
    end = start+ per_page //3+3 = 6
    setProducts(productsData.slice(start,end))

  }
  function searchProduct (productName) 
  {
    console.log(productName);
    let filteredProducts =productsData.filter(product => 
      product.title.toLowerCase().includes(productName.toLowerCase())
      )
    setProducts(filteredProducts)
  }
  return (
    <>
      <p>Page : {pageNo+1}</p>
      <Search onSearch={searchProduct}/>
      <div className='card'>
        <CardList products={products}/>
      </div>
      <button onClick={previousPage} disabled={pageNo<=0?true:false}>&lt; Prev</button> &nbsp;
      <button onClick={nextPage} >Next  &gt; </button>
    </>
  );
}

export default App;




