class Person
{
   vehicle = "Mahindra SUV"
   constructor(name,age)
   {
      this.name = name;
      this.age=age
   }
}
class Employee extends Person
{
   constructor(name,age,salary)
   {
    //this.name = name;
   //this.age=age
    super(name,age)
    this.salary = salary
   } 
}
let e1 = new Employee("amit",30,25000)
console.log(e1.salary);
console.log(e1.name);
console.log(e1.vehicle);