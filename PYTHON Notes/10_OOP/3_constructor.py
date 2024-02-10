class Student:
   institute="ITVedant"
   
   def __init__(self,name,phone):
      print("id of self :",id(self))
      self.st_name = name  #instance variable
      self.st_phone = phone #instance variable
      
   def display(self):
      print("displaying name of student :",self.st_name)
      
      
s1 = Student("prashant","8698562365")
print("id of s1 :",id(s1))

s2 = Student("anuj","8698562345")
print("id of s2 :",id(s2))

print(s1.st_name)
print(s2.st_name)

s1.display()
s2.display()
      
      