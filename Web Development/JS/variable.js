//scope
{
   var a = 10;
   let b = 20;
   const c = 30;
}
console.log(a);
//console.log(b); ERROR
//console.log(c); ERROR

//updation
var d = 10;
console.log("d = ", d);
let e = 20;
console.log("e = ", e);
const f = 30;
console.log("f = ", f);

d = 40;
console.log("d = ", d);
e = 50;
console.log("e = ", e);
//f = 60; ERROR


// re declaration
var g = 10;
var g = "hello"

let h = 40;
//let h = "hello" ERROR due to redeclaration

const i = 50;
//const i = 60; ERROR due to redeclaration


