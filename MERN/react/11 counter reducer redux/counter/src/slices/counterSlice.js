import {createSlice}   from "@reduxjs/toolkit"

const counterSlice=createSlice({
   name:'counters',
   initialState:{count:0},
   reducers:
      {
         incrementByOne:(state,action)=>{return{...state, count:state.count+1}},
         decrementByOne:(state,action)=>{return{...state, count:state.count>0?state.count-1:state.count}},
         incrementByN:(state,action)=>{return{...state, count:state.count+action.payload}},
      },
});

// exporting actions
export const {incrementByOne,decrementByOne,incrementByN} = counterSlice.actions

//exporting entire reducer
export default counterSlice.reducer

//exporting state
export const selectCount = (state) => state.counters.count