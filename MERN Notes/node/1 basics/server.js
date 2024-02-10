// step 1 : import http 
const http = require('http')
let PORT = process.env.PORT

// step 3: handle request and response when someone visits our server
const requestListner =(req,res)=>
{
   res.end("Welcome")
}

// step 2: create server using http
const server = http.createServer(requestListner)

// step 4: provide port number for the server
server.listen(PORT,()=>
{
   console.log(`server is running on http://localhost:${PORT}/`)
})
// step 5: go to console and run this file by typing >node server.js