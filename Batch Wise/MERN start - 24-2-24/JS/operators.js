//arithmatic => +,-,*,/,%,**,++,--
//assignment => =, +=,-=.....
//comparision=> >,<,>=,<=,==,!=,===,!==
//logical   => &&,||,!
//ternary   => ?

console.log("----arithmatic------");
console.log(10+2); //12
console.log(10-2); //8
console.log(10*2); //20
console.log(10/2); //5
console.log(10.0/2); //5
console.log(10/3); //3.33333333
console.log(10%2); //0
console.log(10**2); //100


let x = 10
console.log(x++);
console.log(x);
let y = 20
console.log(++y);

console.log("----ASSIGNMENT------");
let m = 10
m = m+5 //10+5 => 15
console.log(m);
m-=2 //m = m-2 =>15-2 =>13
console.log(m);

console.log("----COMPARISION------");
console.log(10>2);
console.log(10<2);
console.log(10>=2);
console.log(10<=2);
console.log(10!=2);
console.log(10==2);
//== does only content comparision
console.log("12"==12);
//=== does  content+data type comparision
console.log("12"===12);


console.log(5.0===5);


console.log("----LOGICAL------");
//&& : returns true if both conditions are true
//|| : returns true if at least one condition is true
//! :  reverse the result
console.log(10>2 && 10>5);
console.log(10>2 && 10<5);

console.log(10>2 || 10>5);
console.log(10>2 || 10<5);

console.log(!10>5);

console.log("----TERNARY------");
console.log(10>2 ? "yes":"no");