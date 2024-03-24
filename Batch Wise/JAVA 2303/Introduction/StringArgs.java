import java.util.Arrays;

public class StringArgs {
   public static void main(String[] args) 
   {
      System.out.println(args);
      System.out.println(Arrays.toString(args));
      System.out.println(args[0]);
      System.out.println(args[0] instanceof String);
      System.out.println(args[0]+20);
   }
   // public static void main(String[] amey) 
   // {
   //    System.out.println(amey);
   //    System.out.println(Arrays.toString(amey));
   //    System.out.println(amey[0]);
   //    System.out.println(amey[0] instanceof String);
   //    System.out.println(amey[0]+20);
   // }
   
}
