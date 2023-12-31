import React from 'react'
import './Navbar.css'

export default function Navbar() {
  return (
    <>
      <div className='navbar'>
         <img src="https://freepngimg.com/thumb/puppy/33554-2-golden-retriever-puppy-image-thumb.png" alt="" id='left_img'/>
         <div className='filter_pet'>
            <div className='category'>
               <img src="https://freepngimg.com/thumb/cat/22193-3-adorable-cat-thumb.png" alt="" />
               <button>Cat</button>
            </div>
            <div className='category'>
               <img src="https://freepngimg.com/thumb/cat/22193-3-adorable-cat-thumb.png" alt="" />
               <button>Dog</button>
            </div>
            <div className='category'>
               <img src="https://freepngimg.com/thumb/cat/22193-3-adorable-cat-thumb.png" alt="" />
               <button>Bird</button>
            </div>
            <div className='category'>
               <img src="https://w7.pngwing.com/pngs/227/600/png-transparent-goldfish-goldfish-swimming-s-watercolor-painting-photography-orange-thumbnail.png" alt="" />
               <button>Fish</button>
            </div>
         </div>
         <img src="https://freepngimg.com/thumb/cat/22193-3-adorable-cat-thumb.png" alt="" id='right_img'/>
      </div>
     
    </>
  )
}
