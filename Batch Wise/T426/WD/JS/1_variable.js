console.log("Hello javascript");
var age=30;
console.log(age);
console.log("30");

// scope : let and const are blocked scope where as var is not blocked scope 

{
   var a = 10;
   let b = 20;
   const c = 30;
   console.log(a,b,c);
}
console.log(a);
// console.log(b); ERROR
// console.log(c); ERROR

// update : we can only update var and let. we cant update const
var d = 11;
let e = 22;
const f = 33;
console.log(d);
d=111;
console.log(d);

console.log(e);
e=222;
console.log(e);

// f=333; ERROR

// redeclaration : declaring variable with same name
var g = 100;
console.log(g);
var g = 1000;
console.log(g);

let h = 200;
//let h = 2000; //ERROR: can not redeclare block scope variable


const i = 300;
//const i = 3000; //Cannot redeclare block-scoped variable 







