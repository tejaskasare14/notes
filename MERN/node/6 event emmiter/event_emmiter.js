//step 1 : import events
const EventEmmiter=require('events')
//step 2 : create object of EventEmmiter
const eventEmmiter=new EventEmmiter()

//event capturing in simple js:
//const btn = document.getElemetById('btn')
//btn.addEventListner('click',()={code to be execute after click event occur})

//event capturing in node js
//step 3 : capture event
//eventEmmiter.emit('TEST_EVENT') //DO NOT CREATE EVENT BEFORE CAPTURING
//eventEmmiter.on('TEST_EVENT',()=>{console.log('Event is captured');})

//step 4 :create Event
//eventEmmiter.emit('TEST_EVENT')

//creating event before capturing
setTimeout(()=>{
   eventEmmiter.emit('DEMO_EVENT',"data from event emiter")
},0)

eventEmmiter.on('DEMO_EVENT',(data)=>
   {
      console.log('DEMO Event is captured');
      console.log(data);
   })

eventEmmiter.on('DEMO_EVENT',()=>{console.log('DEMO Event is captured');})

module.exports = eventEmmiter