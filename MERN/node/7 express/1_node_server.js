const http=require('http')

const server = http.createServer((req,res)=>
{
   if(req.url=='/') { res.write("Welcome to home") }
   else if(req.url=='/contact') { res.write("Welcome to contact") }
   else { res.write("Not Found") }
   
   res.end()
})

server.listen(4000,()=>
      {
         console.log(`server is running on http://localhost:4000`);
      })