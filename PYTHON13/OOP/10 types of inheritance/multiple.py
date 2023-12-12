class Parent1:
   def p1m(self):
      print("hello I am method of parent 1")
      
   def hello(self):
      print("hello from parent 1")
      
class Parent2:
   def p2m(self):
      print("hello I am method of parent 2")
      
   def hello(self):
      print("hello from parent 2")
      
class Child(Parent2,Parent1):
   pass

c = Child()
c.p1m()
c.p2m()
c.hello() #here hello() method will be called from Parent2 class. because on line number 15 we have mentioned Parent2 first