//for ==> when we know where to stop (end)
//print 1-5 numbers
console.log("print 1-5 numbers");
for(let x=1; x<=5; x++)
{
   console.log(x);
}

console.log("for loop on array");
let marks = [99,98,95,96]
for(let i=0; i<marks.length; i++)
{
   console.log(marks[i]);
}
console.log("for of loop on array");
for(let mark of marks)
{
   console.log(mark);
}

console.log("for in loop on array");
for(let mark in marks)
{
   console.log(mark);
}

console.log("for of loop on string");
let name = "rajubhai"
for(let char of name)
{
   console.log(char);
}

//while =>  when we dont know where to stop (end)
//number guessing game
let my_number = 25
let guessed_number = 0

while(guessed_number!=my_number)
{
   guessed_number = Number(prompt("Enter your number"))
   if(guessed_number>my_number)
      {
         alert(` HINT : Number is less than  ${guessed_number}`)
      }

   else if(guessed_number<my_number)
      {
         alert(` HINT : Number is greater than ${guessed_number}`)
      }
   else{
      alert(" CONGRATULATIONS")
   }
}


//do while
do{
   console.log("it is correct")
}
while(10000<0)

// if we use var in for loop insted of let
for(var p=1; p<=5; p++)
{
   console.log(p);
}

console.log(p);