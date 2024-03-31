public class BreakContinue
{
   public static void main(String[] args) 
   {
      int[] prices = {199,299,199,99,399,299,99,199};
      //dont buy anything with price 99
      for (int price:prices)
      {
         if(price==99)
         {
            continue; // towards line no 7 
            //System.out.println("hello"); ERROR
         }
         else
         {
            System.out.println(price + " added to cart");
         }
      }
   }
}