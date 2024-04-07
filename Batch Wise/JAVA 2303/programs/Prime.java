import java.util.Scanner;
public class Prime
{
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      System.out.print("Enter number :");
      int x = sc.nextInt();
      boolean is_prime = true;
      //start :2, end = x-1
      for(int i = 2; i<x; i++)
      {
         if(x%i==0) //6%2==0
         {
            is_prime=false;
            break;
         }
      }
      if(is_prime)
      {
         System.out.println(x + " is prime number");
      }
      else
      {
         System.out.println(x + " is not prime number"); 
      }


   }
}