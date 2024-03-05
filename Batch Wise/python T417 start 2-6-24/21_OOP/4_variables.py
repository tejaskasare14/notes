class Student:
   college_name="IIT" # college_name : static variable
   def __init__(self,name,phone):
      self.sname = name #self.sname : instance variable
      self.sphone = phone #self.sphone : instance variable
      
   def demo(self):
      laptop = "HP" #laptop : local varible
      print(laptop)
      #print(self.laptop)
      
   def display(self):
      print(self.college_name)
      print("static using class name :",Student.college_name)
      print(self.sname)
      print(self.sphone)
      self.demo()
      #print(laptop)
      #print(self.laptop)
      
s1 = Student("raj",8956985412)
s1.display()
print(s1.college_name)
print(Student.college_name)