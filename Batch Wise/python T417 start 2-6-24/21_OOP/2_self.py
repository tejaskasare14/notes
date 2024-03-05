class Student:
   age = 10
   def display(self):
      print("id of self = ",id(self))
s1 = Student()
print("id of s1 =   ",id(s1))
s1.display()

s2 = Student()
print("id of s2 =   ",id(s2))
s2.display()

