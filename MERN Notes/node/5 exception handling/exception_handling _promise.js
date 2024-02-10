//util function is used to conver error first callback function into promise
//error first callback function means function like readFile (we have seen in last code)
const util = require('util')
const fs = require('fs')
const files = ['./city.txt','./employee.txt','./names.txt']
//converting return type readFile into promise
const readFile=util.promisify(fs.readFile)
const writeFile=util.promisify(fs.writeFile)
//converting all functions at time into promise
// const fs = require('fs').promises
// fs.readFile()
function main()
{
   files.forEach(async(file)=>
      {
         try
            {
               let data = await readFile(file)
                console.log(data);
                //to write data into file
               let new_file = await writeFile('./demo.txt',"add this into demo.txt file")     
            }
            catch(err)
            {
               console.log(file, " not found");
             }
      })
}
main()
console.log("done");