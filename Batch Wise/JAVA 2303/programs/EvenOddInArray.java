public class EvenOddInArray {
   public static void main(String[] args) {
      int[] data = {65,24,3,91,12};
      for (int num:data)
      {
         if(num%2==0)
         {
            System.out.println(num + " is even");
         }
         else
         {
            System.out.println(num + " is odd");
         }
      }
   }
   
}
