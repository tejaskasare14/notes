console.log("hi");
//SCOPE
{
   var a = 10;
   let b = 20;
   const c = 30;
}
console.log(a);
//console.log(b);
//console.log(c);

function add()
{
   var d = 10;
}
//console.log(d);

//UPDATE
var e = 10;
e =15;
console.log(e);

let f=40;
f=50
console.log(f);

const g=50;
g=60;
//console.log(g);

//REDECLARATION
var h = 10;
var h = "hi"

let i = 50;
//let i = "hello"

const j = 60;
//const j="bye"