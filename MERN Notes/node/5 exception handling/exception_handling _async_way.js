const fs = require('fs')
const files = ['./city.txt','./employee.txt','./names.txt']

files.forEach(file=>
   //readFile() is used to read files in async way. in simple language, readFile() is async function
   //if you are using callback function as a parameter in async function then callback function must be last parameter of that async function
   //if you have callback function as a last parameter then first parameter of that callback function must be error
   fs.readFile(file,(err,data)=>{
      // console.log(err);
      // console.log(err && err.code);
      //after reading each file, we will get error and data. if there is no error, then will get null
      //since null is not having any CODE parameter, we have to check error code with : err && err.code
      if(err && err.code == "ENOENT")
         {
            console.log(file, " not found");
         }
      console.log(data);
   })
   )
   console.log("done");