const express = require('express')
const app = express()

app.use(express.static('public'))
app.use(express.static('node_modules/bootstrap/dist'))

app.set('view engine','ejs')

//creating application mw
app.use((req,res,next)=>{
   console.log("Application mw called before every request");
   req.country = "India"
   next()
})

//creating routing mw
const authenticate = (req,res,next)=>{
   if (req.query.apikey && req.query.apikey=="123")
   {
      next()
   }
   else
   {
      res.status(401).send("you are not authorised")
   }
}

app.get('/',(req,res)=>
            {
               //send() is combination of write() and end()
               //res.send("Welcome to home")
               //if you have query parameter (?) in url then get it by :
               //http://localhost:4000/?name=tejas&age=28
               //console.log(req.query);
               //res.sendFile(__dirname + '/index.html') //__dirname gives path of current dir/folder
               console.log(req.country);
               res.render('index',{name:'Tejas'})
               //in above line index means we are pointng to index.ejs in views folder
            })
            
app.get('/contact',authenticate,(req,res)=>
            { 
               //res.send("Welcome to contact") 
               res.sendFile(__dirname + '/contact.html')
            })

app.get('/users/:id',(req,res)=>
            { 
               console.log(req.country);
               console.log(req.params); 
                const id=Number(req.params.id)
                console.log(id);
                if(isNaN(id))
                {
                  res.send(`Plese enter valid id`) 
                }
                else
                {
                  res.send(`we have got user with id : ${req.params.id}`) 
                }
               
              
            })

//wild card routing must be at the end
app.get('**',(req,res)=>{ res.send("This url does not exist") })

app.listen(4000,()=>{console.log(`server is running on http://localhost:4000`);})