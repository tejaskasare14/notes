//if
//check given number is even
let a = 13
if(a%2==0)
{
   console.log(a, "is even");
}

//if else
// check given number id positive or negative
let b = -12
if(b>0)
{
   console.log(b, " is positive");
}
else
{
   console.log(b, " s negative");
}

//multiple condiditons
let x=100
let y=50
let z = 15

if(x>y && x>z)
   {
      console.log(x, "is greater");
   }
else if(y>x && y>z)
   {
      console.log(y, "is greater");
   }
else
   {
      console.log(z, "is greater");
   }


// grading example
// let marks=prompt("Enter your marks")
//console.log(marks);
//console.log(marks+2);

let marks=Number(prompt("Enter your marks"))
if(marks>91 && marks<=100)
{
   alert(`You have got A+ grade ${marks}`)
}
else if(marks>81 && marks<=90)
{
   alert("You have got C grade")
}
else
{
   alert("FAILED")
}

// switch case
// sunday - 0 , monday -1 ......
let day_number = 3
switch (day_number) {
   case 0:
      console.log("Sunday");
      break;
   case 1:
      console.log("Moday");
      break;
   case 2:
      console.log("Tuesday");
      break;
   case 3:
      console.log("Wed");
      break;
   case 4:
      console.log("Thurs");
      break;
   case 5:
      console.log("Fri");
      break;
   case 6:
      console.log("Sat");
      break;

   default:
      console.log("enter correct choice between 0-6");
      break;
}
