const eventEmmiter = require('./event_emmiter');

eventEmmiter.on('DEMO_EVENT',(data)=>
   {
      console.log('DEMO Event is captured in different file');
      console.log(data);
   })