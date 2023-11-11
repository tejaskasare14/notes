//REST must be last in destucting pattern

// rest on array
let marks = [95,98,92,96]
let [django, ...rest_marks]=marks

//let [angular, ...rest_marksss, spring]=marks  => ERROR => A rest element must be last in a destructuring pattern
console.log(django);
console.log(rest_marks);

// rest on object
let emp = {
   name:"raj",
   age:25,
   salary:25000
}

let {name, ...rest_details} = emp
console.log(name);
console.log(rest_details);

// rest in function parameter
function add(n1,n2, ...rest_numbers)
   {
      console.log(n1);
      console.log(n2);
      console.log(rest_numbers); //array
   }

add(10,20,30,40,50)












