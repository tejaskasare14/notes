//named function
function add(x,y)
{
   result = x+y //10+20
   console.log(result);
}

add(10,20) //x=10,y=20
add(1,20) //x=1,y=20
add(10,2) //x=10,y=2

//anonymous
const sub =function (p,q) 
               {
                  result = p-q 
                  console.log(result);
               }
sub(10,2) //p=10, q=2


//arrow function
const div =(a,b)=>
   {
      result = a/b 
      console.log(result);
   }
div(10,2)
div(1510,3)