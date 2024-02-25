console.log("hello javascript");
//variable : is used to store data
// in js we can declare variable with 3 prefix
// var,let or const

//scope : we can access only var outside of a scope
{
   var a = 10;
   let b = 20;
   const c = 30;
}
console.log(a);
// console.log(b); ERROR
// console.log(c); ERROR

//update: we can only update var and let
var d = 11;
let e = 22;
const f = 33;

console.log(d);
d = 44
console.log(d);

console.log(e);
e = 55
console.log(e);

console.log(f);
//f = 66 ERROR
console.log(f);

//re declaration : we can only re declare var
var g = 100
var g = "hello"
console.log(g);


let h = 100
//let h = "hello" ERROR

const i = 100
//const i = "hello" ERROR
