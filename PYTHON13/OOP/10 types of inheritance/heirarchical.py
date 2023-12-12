class Parent:
   x = 10 
   def display(self, name):
      print("Hello ", name)
      
class Child1(Parent):
   pass

class Child2(Parent):
   pass

c1 = Child1()
print(c1.x)
c1.display("Child 1")

c2 = Child2()
print(c2.x)
c2.display("Child 2")