const fs = require('fs')
const files = ['./city.txt','./employee.txt','./names.txt']
files.forEach(file=>{
   try
   {
      //const data=fs.readFileSync(file) //you can read file without encoding : so you will get only file not found exception
      //const data=fs.readFileSync(file,'utf-8') //you can read file with encoding : so you will only get file not found exception
      const data=fs.readFileSync(file,'utf-22') //with wrong encoding :  you will only get 2 exceptions,  encoding and file not found
                                                
      console.log(data);
   }
   catch(err)
   {
      //console.log(err.code);
      //console.log(err.code);
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