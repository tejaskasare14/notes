public class Test 
{
   public static void main(String[] args) {
      System.out.println(10+2);
      System.out.println(10.2+2);
      System.out.println(10*2);
      System.out.println(10-2);
      System.out.println(10/2);
      System.out.println(10.0/2);

      System.out.println("hi"+2);
      System.out.println(10+2+"hi"+20);

      int x = 10;
      System.out.println(x++);
      System.out.println(x);

      int y = 20;
      System.out.println(++y);

      int p = 30;
      int q = 40;
      System.out.println(p++ + ++q + p);

      int a = 15;
      a = a + 10; //15 + 10 = 25

      System.out.println(a);

      a-=5; //a = a - 5
      System.out.println(a);


   }
}