public class ForLoop {
   public static void main(String[] args) {
      //initialization - condition - inc/dec - statements (code/body)
      //for(initialization ; condition ; inc/dec) {statements}
      //print 1 to 5 numbers
      System.out.println("print 1 to 5 numbers");
      for(int i=1; i<=5; i++)
      {
         System.out.println(i);
      }
      //print 5 to 1 numbers
      System.out.println("print 5 to 1 numbers");
      for(int i=5; i>=1; i--)
      {
         System.out.println(i);
      }

      //for loop on string and array
      System.out.println("for loop on string");
      String name = "amit";
      for (int i=0; i<name.length(); i++)
      {
         System.out.println(name.charAt(i));
      }

      System.out.println("for loop on array");
      int marks[] = {95,96,93,99};
      for(int i=0; i<marks.length; i++)
      {
         System.out.println(marks[i]);
      }

      System.out.println("for each loop on array");
      for(int mark:marks)
      {
         System.out.println(mark);
      }

   }
}
