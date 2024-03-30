public class ReferenceVariable 
{
   public static void main(String[] args) 
   {
      new ReferenceVariable(); //useless object
      ReferenceVariable rv = new ReferenceVariable();  //rv is reference variable
      rv.demo(); //accessing memebrs of object using reference variable
     
   }
   
  public void demo()
   {
      System.out.println("Hello Demo");
   }

}
