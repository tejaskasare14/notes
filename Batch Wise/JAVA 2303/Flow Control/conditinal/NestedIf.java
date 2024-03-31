public class NestedIf {
   public static void main(String[] args) {
      int x = 21;
      if(x%3==0)
      {
         if(x%2==0)
         {
            System.out.println(x+ " is divisible by 3 and it is even");
         }
         else
         {
            System.out.println(x+ " is divisible by 3 but it is not even");
         }
      }
      else
      {
         System.out.println(x + " is not divisible by 3");
      }
   }
   
}
