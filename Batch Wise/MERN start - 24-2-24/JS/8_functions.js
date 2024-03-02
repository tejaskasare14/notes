//function :  block of code execute only when we call it
//use case :  to eliminate duplicate code 
//we can call a function as many time we want
//function has 3 types in js :
   //named function
   //anonymous function
   //arrow function

function add() //function defination
{
   let x = 10;
   let y = 20;
   let result = x+y;
   console.log(result);
}
add(); //function calling
add();
add();

//parameters & arumnets
//parameter : value required for the finction
//arguments : value pass to the finction
function sub(x,y) //x,y are parameter
{
   let result = x-y 
   console.log(result)
}
sub(10,2) //10, 2  are arguments
sub(10,20)

//return keyword : use when we want to access function variable outside of function
//output of one function act as input to another
function div(){
   var x=100;
   let y=20;
   const result=x/y;
   console.log(result);
   return result;
}
div()
console.log(div());
console.log(div());
//console.log(result);
output = div()
console.log(output);
console.log(output);

//anonymous function
let join_name=function (fname,lname) 
               {
                  console.log(`full name is ${fname} ${lname}`);
               }
join_name("steve","jobs")

//arrow function
let multi =(x,y) => {
                        console.log(x*y);
                     }
multi(10,2)

