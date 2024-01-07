class Person: 
   @staticmethod
   def static_m1_add(x,y):
      result = x+y
      print(result) #25
      Person.static_m2_sub(result,15) #25,15
      
   @staticmethod
   def static_m2_sub(x,y):
      result = x-y
      print(result)
      
   @staticmethod
   def static_m3():
      print("hello from static_m3")

p1 = Person()
p1.static_m1_add(10,15)
Person.static_m3()