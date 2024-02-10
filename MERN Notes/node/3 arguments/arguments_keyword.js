//function main( exports , require , module , __filename,__dirname) {

   let a = 20 //this will not be accissible outside of the file
   console.log(arguments);
   module.exports.a = 20  //way 1 of exporting 
   exports.b = 30 //way 2 of exporting 
   exports.emp = {name:"raj",salary:35000} //exporting object
   exports.marks=[99,98,95] //exporting array
   exports.add =function add_num(){} //exporting function
   exports.city="mumbai" //exporting string

   //return module.exports
   //return exports
//}
