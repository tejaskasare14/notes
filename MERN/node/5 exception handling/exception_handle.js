const fs = require('fs')
const files = ['./city.txt','./employee.txt','./names.txt']
files.forEach(file=>{
   try
   {
      //const data=fs.readFileSync(file) //without encoding so you will only get file not found exception
      //const data=fs.readFileSync(file,'utf-8') //with correct encoding so you will only get file not found exception
      const data=fs.readFileSync(file,'utf-22') //with wrong encoding so you will only get 2 exceptions, 
                                                //encoding and file not found
      console.log(data);
   }
   catch(err)
   {
      //console.log(err);
      if(err.code=='ENOENT')
      {
         console.log("file does not exist");
      }
      else if(err.code=='ERR_INVALID_ARG_VALUE')
      {
         console.log('invalid encodeing');
      }
   }
})