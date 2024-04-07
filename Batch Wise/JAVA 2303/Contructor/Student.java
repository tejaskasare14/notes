public class Student {
   String student_name;
   int student_age;
   String studen_phone;

  public Student(String name, int age,String phone)
  {
      this.student_name = name;
      this.student_age = age;
      this.studen_phone=phone;
  }

   public static void main(String[] args) {
      // Student s1 = new Student();
      // Student s2 = new Student();
      // s1.student_name="raju";
      // s2.student_name = "rani";
      // System.out.println(s1.student_name);
      // System.out.println(s2.student_name);

      Student s1 = new Student("raju",20,"7865845236");
      Student s2 = new Student("rani",25,"7856856558");
      System.out.println(s1.student_name + " "+ s1.student_age + " "+ s1.studen_phone);
      System.out.println(s2.student_name + " "+ s2.student_age + " "+ s2.studen_phone);
   }
}
