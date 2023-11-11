// descructor on array
let marks = [95,98,92,96]
console.log(marks);

let [py,java,sql,react] = marks
console.log(py);

let [djngo,angular,,spring] = marks
console.log(angular);

// descructor on object
let emp = {
   name:"raj",
   age:25,
   salary:25000
}


let {name} = emp // getting only name from emp object
console.log(name);

//descructor on object with function
function emp_fun({salary}) //getting only salary from emp object
{
   console.log(salary);
}

emp_fun(emp)


//descructor on Math (built in objects)
console.log(Math.random()); // without destruction
console.log(Math.floor(4.9999));  // without destruction

let {random,floor} = Math // with destruction
console.log(random());
console.log(floor(5.9999));