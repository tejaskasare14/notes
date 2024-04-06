import java.util.Scanner;
public class WhileLoop {
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      String og_password = "tejas123";
      String password="";
      while(og_password!=password)
      {
         System.out.print("Enter your password-");
         password = sc.nextLine();
         System.out.println(password);
         if(og_password.equals(password))
         {
            System.out.println("Welcome Tejas");
            break;
         }
      }
      System.out.println("Out of the loop");
   }
}
