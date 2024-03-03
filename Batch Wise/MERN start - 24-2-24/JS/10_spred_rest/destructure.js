//destrucuring : unpacking of values from array
//or properties of object into disctinct variable

let emp = {name:"raj",salary:25000,city:"pune"}

// function emp_details(name,salary)
// {
//    console.log(name);
//    console.log(salary);
// }
// emp_details(emp.name,emp.salary)
function emp_details({name,salary})
{
   console.log(name);
   console.log(salary);
}
emp_details(emp)
//desctruring of  properties of object
let {name,salary} = emp
//desctruring of an array values
let marks = [95,96,98,94]
let [py,sql,,spring] = marks
console.log(py);
console.log(spring);