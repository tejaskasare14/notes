class Employee
{
   
   emp_age;
   emp_salary=0;
   static company_name = "TATA"
   constructor(name,age,salary)
   {
      this.emp_name = name
      this.emp_age = age
      this.emp_salary = salary
   }

   emp_details()
   {
      console.log(`Employee name is ${this.emp_name}`);
   }

   static test()
   {
      console.log('this is static method of class');
   }
}

const emp_obj1 = new Employee("raj",30,25000)
const emp_obj2 = new Employee("rani",31,35000)
emp_obj1.emp_details()
emp_obj2.emp_details()

console.log(Employee.company_name);
Employee.test()