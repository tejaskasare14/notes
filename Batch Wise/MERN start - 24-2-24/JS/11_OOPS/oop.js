class Student
{
   name="" //property -> variable
   age=0   //property -> variable
   static course_name = "MERN ESSN."
   constructor(_name,_age)
   {
      this.name = _name
      this.age = _age
   }

   studying() //behaviour -> function
   {
      console.log(`${this.name} study for 3 hrs a day`);
   }
}
let s1 = new Student("raj",30) 
//Student() is an object
//s1 is RV used to access properties and behaviours of object
let s2 = new Student("rani",25) 
console.log(s1.name);
console.log(s2.name);

s1.studying()
s2.studying()

console.log(Student.course_name);
console.log(Student.course_name);