let a=10;
console.log(typeof(a));
let b=20;
console.log(typeof(b));
let c=99999999999999999n;
console.log(typeof(c));

let d='s'
console.log(typeof(d));
let e ="hello"
console.log(typeof(e));
let name = "raj"
let f=`bye ${name}`
console.log(f);
console.log(typeof(f));

let g=true
console.log(typeof(g));

let h;
console.log(typeof(h));

let i = null
console.log(typeof(i));

let j = [10,15.3,"hello"]
console.log(typeof(j));

let k = {name:"raju"}
console.log(typeof(k));


// array data type
console.log("----- more on array data type ---");
let m = [10,20,[55,66],30,{age:30,marks:99}]
console.log(m.length);
console.log(m[0]);
console.log(m[2]);
console.log(m[2][1]);
console.log(m[4]);
console.log(m[4].age);
console.log(m[7]);

let n = [10,20,11,22,33]
n.push(30)
console.log(n);
n.unshift(40)
console.log(n);
n.pop()
console.log(n);
n.shift()
console.log(n);

console.log(n.includes(25));
console.log(n.indexOf(11));
console.log(n.slice(0,2));

//object data type
let city = "thane"
let salary = 35000
let emp = {
   name:"aniket",
   age:30,
   city:city,
   salary, //short hand property  
   add:(x,y)=>{console.log(x+y)} ,//function inside object
   department : ["teacher","hr"]
}
console.log(emp);

emp["id"] = "ABV78" //dynamic property
console.log(emp);
emp.add(55,1)
console.log(emp);
console.log(emp.department[0]);



 