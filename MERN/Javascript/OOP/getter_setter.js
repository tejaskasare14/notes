class Employee
{
   static company_name = "TATA"
   constructor(name,age,salary)
   {
      this.emp_name = name
      this.emp_age = age
      this.emp_salary = salary

      let city="pune";
   }

   city_name()
   {
      console.log(this.city);
   }

   get cityname()
   {
      return this.city;
   }

   set cityname(city_name)
   {
      this.city = city_name
   }

}

const emp = new Employee("raju",25,23500)
console.log(emp.emp_name);
console.log(emp.city); //we cant access city since it is private
emp.city_name();
emp.cityname = "thane"
console.log(emp.cityname);