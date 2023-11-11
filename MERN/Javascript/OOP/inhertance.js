class Person
{
   constructor(name,age)
   {
      this.person_name = name
      this.person_age = age
   }
}

class Employee extends Person
{
   constructor(name,age,salary)
   {
      //this.emp_name = name
      //this.emp_age = age
      super(name,age) // here name is initialized by parent class constructor
      this.emp_salary = salary
   }
}

const emp = new Employee("raj",32,25000)
console.log(emp.person_name);
console.log(emp.person_age);
console.log(emp.emp_salary);