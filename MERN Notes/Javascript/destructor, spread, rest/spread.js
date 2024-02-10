// spread on array
let data1 =[11,22]
let data2 =[111,222]
let data3 = [...data1,...data2] //with spread  [11, 22, 111, 222]
let data4 = [data1,data2] //without spread [[11, 22], [111, 222]]
console.log(data3);
console.log(data4);

//we can user sread in between
let data5 = [10,20, ...data1, 30, 40, ...data2]
console.log(data5);

//spread on object
let obj1 = {name:"raj",city:"pune"}
let obj2 = {age:32}

let emp = {...obj1, ...obj2}
console.log(emp);

let emp_without_spread= {obj1,obj2}
console.log(emp_without_spread);


//spread on function
function add_n(...numbers)
{
   console.log(numbers);
   sum = 0
   for (n of numbers)
   {
      sum+=n
   }
   console.log(sum);
}

add_n(10,20,30)

