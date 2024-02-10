console.log("Hello Node"); // 1.call stack(is there cb? NO) -> 2.execute

//3. call stack(is there cb? YES) -> 4.node api and wait till 2 seconds -> 5. after 2 sec go to callback queue
setTimeout(
   function im_timeout()
   {
      console.log("Iam timeout");
   },2000)

//6. call stack(is there cb? NO)-> 7. execute
console.log("Bye Node 1");
//8. call stack(is there cb? NO)-> 9. execute
console.log("Bye Node 2");

//this is end of program so event loop check for callback queue, and for now we have im_timeout
//waiting in callback queue, so it will go in 10. call stack -> 11. execute
