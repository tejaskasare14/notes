//... => called as spred operator
//spread on array
data1 = [10,20]
data2 = [11,22]
data3 = [data1,data2]
console.log(data3); //[[10,20],[11,22]] NOT SPRED
data4 = [...data1, ...data2]
console.log(data4);
data5 = [...data4,99,...data1,33,...data2]
console.log(data5);

//spread on object
data6 = {name:"raj",age:30}
data7 = {salary:35000,city:"pune"}
x = {data6,data7}
console.log(x);
emp = {...data6,...data7}
console.log(emp);