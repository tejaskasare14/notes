class Demo:
   def display(self,name,age):
      print(name,age)
      print("i am first display")
      
   def display(self,salary,city): #this method will override previos display method
      print(salary,city)
      print("i am second display")
      
   def display(self,phone):  #this method will override previos 2 display methods, we can Demo has only 1 display method(even we have written total 3 methods)
      print(phone)
      print("i am third display")
      
d =Demo()
d.display("raj",30) # we will get error
d.display(35,"hello")
d.display(True,[10,20,"hello"])