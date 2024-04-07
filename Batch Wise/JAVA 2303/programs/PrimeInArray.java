public class PrimeInArray {
   public static void main(String[] args) {
      int[] data = {65,24,3,91,12};
      boolean is_prime=true;//false
      for (int num:data)
      {
         for(int i=2; i<num; i++)
         {
            if(num%i==0)//24%2==0
            {
               is_prime=false;
               break;
            }
         }
         if(is_prime){ System.out.println(num + " is prime"); }
         else{System.out.println(num + " is not prime");}

         is_prime=true;
      }
   }
   
}
