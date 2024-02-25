//if, else if(n), else
//check given number is even or odd

let a = 203
//let a = prompt("Enter a number")
if(a%2==0)
   {
      console.log(`${a} is even`);
   }
else
   {
      console.log(`${a} is odd`);
   }

//check given number is two digit number
let b = 653
if (b>9 && b<100)
   {
      console.log(`${b} has 2 digits`);
   }
   else
   {
      console.log(`${b} is not 2 digit`);
   }

//largest among 3 numbers
let x=100, y=50, z=30
if(x>y && x>z)
   {
   console.log(`${x} is greater`);
   }
else if(y>x && y>z)
   {
   console.log(`${y} is greater`);
   }
else
   {
      console.log(`${z} is greater`);
   }

   //switch case
   //sun - 0, mon - 1 .......
   let day_number = Number(prompt("enter a number"))
   switch (day_number) {
      case 0:
         alert("Today is sunday")
         break;
      case 1:
         alert("Today is monday")
         break;
      case 2:
         alert("Today is tuesday")
         break;
      case 3:
         alert("Today is wednesday")
         break;
      case 4:
         alert("Today is thursday")
         break;
      case 5:
         alert("Today is friday")
         break;
      case 6:
         alert("Today is saturday")
         break;     
      default:
         alert("Enter number between 0 to 6")
         break;
   }
