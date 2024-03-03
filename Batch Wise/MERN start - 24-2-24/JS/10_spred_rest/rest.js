//rest on array
let prices=[99,199,299]
let [candy,potato,jilebi]=prices
console.log(candy);
console.log(potato);
console.log(jilebi);

console.log("---using rest----");
let [tomato,...rest_prices]=prices
console.log(tomato);
console.log(rest_prices);

//rest on object
let student = {name:"raj",age:21,city:"pune"}
let {name,...rest_details}=student
console.log(name);
console.log(rest_details);

//rest must be last
// data1 = [10,20,30,40,50]
// let [a,...rest_data1,b] = data1 //A rest element must be last in a destructuring pattern
// console.log(a);
// console.log(rest_data1);

//rest in function parameter
function demo(a,...b)
{
   console.log(a);
   console.log(b);
}
demo(20,30,40)
