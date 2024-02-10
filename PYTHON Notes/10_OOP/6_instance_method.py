class Person:
   def __init__(self,name):
      self.name = name
      self.age=30
      
   def instance_m1(self):
      print("hello I am instance_m1()")
      print("m1: ",self.name)
      self.instance_m2() # to line 11
      
   def instance_m2(self):
      print("hello I am instance_m2()")
      print("m2: ",self.name)
      
p1 = Person("prashant")
p1.instance_m1() #to line 6

p2 = Person("aniket")
p2.instance_m1()
      