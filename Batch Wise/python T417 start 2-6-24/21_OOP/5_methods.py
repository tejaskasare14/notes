class Car:
   wheels = 4 #class varibale
   def __init__(self,name,brand):
      self.cname = name #instance variable. self.cname = "i10"
      self.cbrand = brand #instance variable. self.cbrand="hyndai"
      
   def changeCarName(self,new_name): #intance method
      self.cname = new_name #here self.cname = "i10" will change to self.cname = "i20"
      #print(self.cname)
      
   
   @classmethod  #decorator 
   def changeWheelNumber(cls,new_wheels):#class method
      cls.wheels = new_wheels
      print(cls.wheels)
      print(Car.wheels)
   
   @staticmethod 
   def generalUtilityMethod():
      print("hello I am static method")

c1 = Car("i10","hyndai")#name=i10, brand=hyndai to line no 3
print(c1.cname) #i10
c1.changeCarName("i20")
print(c1.cname) #i20

print(c1.wheels) #4
print(Car.wheels) #4
c1.changeWheelNumber(6)
Car.changeWheelNumber(8)

c1.generalUtilityMethod()
  





      