import java.util.Arrays;
public class JavaArray {
   public static void main(String[] args) {
      int[] marks1 = new int[3];
      int marks2[] = new int[3];
      int []marks3 = new int[3];

      marks1[0] = 95;
      marks1[1] = 96;
      marks1[2] = 99;
      //marks1[3] = 99; ArrayOutOfBondException

      System.out.println(marks1);
      System.out.println(Arrays.toString(marks1));

      int[] ages1 = {15,25,36};
      int ages2[] = {14,25,37};
      int []ages3 = {10,20,31};

      System.out.println(ages1);
      System.out.println(Arrays.toString(ages1));

      String[] names = {"raj","rani"};
      System.out.println(names);
      System.out.println(Arrays.toString(names));

   }
}
