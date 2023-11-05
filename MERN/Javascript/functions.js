// function => named,anonymous,arrow
//named function
function add(x,y) //x,y are parameters
{
   var result = x+y
   console.log(result);
}

add(10,20)//10,20 are arguments
// console.log(result); cant access var outside of function scope
// add(30)  NaN
// add() 


//return => if we want pass result of function, outside a function
function sub(p,q)
{
   let result = p-q 
   return result
}
sub(10,5)
console.log(sub(20,5));
console.log(sub(50,5));
let output = sub(60,10) //when we use return, store function call into varible
console.log(output);
console.log(output);
console.log(output+50);

// anonumous function
let multi = function (a,b) 
               {
                  let result = a*b 
                  return result;
               }

multi(10,2)
console.log(multi(10,3));
let multiplication = multi(10,5)
console.log(multiplication);

// arrow function
let div = (r,s) => 
                  {
                     let result = r/s 
                     console.log(result);
                  }

div(600,23)