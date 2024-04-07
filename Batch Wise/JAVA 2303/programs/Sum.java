public class Sum {
   public static void main(String[] args) {
      int[] data = {1,5,2,3,4};
      int total=0;//0+1=1 1+5=6 6+2=8 8+3=11 11+4=15
      for(int num:data)
      {
         total+=num; //total=total+num
      }
      System.out.println("Sum is: "+total);
   }
}
