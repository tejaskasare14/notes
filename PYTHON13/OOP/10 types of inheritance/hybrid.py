class Parent:
   x = 10 
   def display(self, name):
      print("Hello ", name)
      
class Child1(Parent):
   def greeting(self):
      print("Hello from Child 1")

class Child2(Parent):
   pass

class Child(Child1):
   pass

c = Child()
print(c.x)
c.display("I am grand child")
c.greeting()