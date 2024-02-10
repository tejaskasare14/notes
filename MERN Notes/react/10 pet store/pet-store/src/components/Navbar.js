import React, { useState } from 'react'
import './Navbar.css'
import { useFetchApi } from '../hooks/useFetchApi'

export default function Navbar(props) {
   let [pet_type,setPetType] = useState('')
   const changePetType= (petType) =>
   {
         () => setPetType(petType)
         props.onFilter(pet_type)
   }
  return (
    <>
      <div className='navbar'>
         <img src="https://freepngimg.com/thumb/puppy/33554-2-golden-retriever-puppy-image-thumb.png" alt="" id='left_img'/>
         <div className='filter_pet'>
            <div className='category'>
               <img src="https://freepngimg.com/thumb/cat/22193-3-adorable-cat-thumb.png" alt="" />
               <button onClick={() => changePetType("cat")}>Cat</button>
            </div>
            <div className='category'>
               <img src="https://freepngimg.com/thumb/cat/22193-3-adorable-cat-thumb.png" alt="" />
               <button onClick={() => changePetType("dog")}>Dog</button>
            </div>
            <div className='category'>
               <img src="https://freepngimg.com/thumb/cat/22193-3-adorable-cat-thumb.png" alt="" />
               <button onClick={() => changePetType("bird")}>Bird</button>
            </div>
            <div className='category'>
               <img src="https://w7.pngwing.com/pngs/227/600/png-transparent-goldfish-goldfish-swimming-s-watercolor-painting-photography-orange-thumbnail.png" alt="" />
               <button onClick={() => changePetType("fish")}>Fish</button>
            </div>

            <div className='category'>
               <img src="https://w7.pngwing.com/pngs/227/600/png-transparent-goldfish-goldfish-swimming-s-watercolor-painting-photography-orange-thumbnail.png" alt="" />
               <button onClick={() => changePetType("all")}>All</button>
            </div>

         </div>
            
        
         
         
         
         <img src="https://freepngimg.com/thumb/cat/22193-3-adorable-cat-thumb.png" alt="" id='right_img'/>
      </div>
      
     
    </>
  )
}
