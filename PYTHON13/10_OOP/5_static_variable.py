class Test:
   a = 5 #creating static variable inside a class and outside of all methods
   
   def instance_method(self):
      Test.b = 11
   
   @classmethod   
   def class_method(cls):
      cls.c = 30
      Test.d = 40
   
   @staticmethod
   def static_method():
        Test.e = 999
        
   def __init__(self):
      Test.f = 1000
      
t1 = Test()
print(t1.a , Test.a)
t1.instance_method()
print(t1.b , Test.b)
t1.class_method()
print(t1.c, Test.c)
print(t1.d, Test.d)
t1.static_method()
print(t1.e, Test.e)
print(t1.f, Test.f)

t1.h = 300 #instance variable
Test.i = 3000 #static variable
print(t1.h)
#print(Test.h)#we cant call/access h using class name because it is not static variable. it is instance variable(why? becuase it is declred using rv)
print(t1.i, Test.i)

      

   