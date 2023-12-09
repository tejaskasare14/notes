class Person:  
   city ="thane"
   
   @classmethod
   def class_m1(cls):
      print("hello I am class_m1()", Person.city)
      cls.class_m2() # to line 11
      Person.class_m3() # to line 15
   
   @classmethod  
   def class_m2(cls):
      print("hello I am class_m2()")
      
   @classmethod  
   def class_m3(cls):
      print("hello I am class_m3()")
      
p1 = Person()
p1.class_m1() # to line 5
Person.class_m1()
