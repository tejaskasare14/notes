//numeric : Number
//charcters : string
//yes/no : boolean
//collection : string, array, object
//others : null, undefained
var a = 10;
console.log(a);
console.log(typeof(a));
console.log(typeof(12));
console.log(typeof(12.5));

console.log(typeof('s'));
console.log(typeof("hello"));
let age = 25;
console.log(`my age is age`);
console.log(`my age is ${age}`);
console.log(typeof(`my age is ${age}`));


console.log(typeof(true));

//array
//1. collection of heterogenous elemets
//2. duplicates allowed
//3. []
//4. size - no limit
let arr  = [10,20,"hello",10]
console.log(arr);
console.log(typeof(arr));
arr.push(40) //add element at the end
console.log(arr);
arr.unshift(50) //add element at the start
console.log(arr);
arr.pop() //remove element from the end
console.log(arr);
arr.shift() //remove element from the start
console.log(arr);

//access array items : by using index
console.log(arr[0]);
console.log(arr.length);
console.log(arr[4]); //undefined
//in js which is not exist, considred as undefined
console.log(arr.indexOf(10)); //0
console.log(arr.indexOf(100)); //-1

//object:
//collection of data in key value pair
name = "raj",
city = "thane"
employee = {
   name:name,
   city,//short hand property: when key and variable has same name
   salary:25000,
   accounts:["ICIC","HDFC"],
   address:{landmark:"antop hill",pincode:126642}
}
//we can access object elements by using key
console.log(employee.name);
console.log(employee.city);
console.log(employee.salary);
console.log(employee.accounts[1]);
console.log(employee.address.landmark);

employee['phone']="9856589564" //dynamic property of object
console.log(employee.phone);

//undefined
var account_number;
console.log(account_number); //undefined


//variable housting
//we can access var variable before declaring 
console.log(bank_account);
var bank_account;


//we cant access let variable before declaring 
//console.log(new_address); //ERROR
//let new_address;


//null
var data = null //not pointing to any data type
console.log(data);