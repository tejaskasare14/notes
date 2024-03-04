class Car: #class
   name = "honda" #property -> variable
   price = 25000
   
   def start_car(self,password): #behaviour -> method
      if password==123:
         print(self.name)
         print("car is starting ......bruuuummmmmm")
      else:
         print("Worng password")  
Car() #object -> useless object (there is no reference variable)
c1 = Car() #c1 is reference variable
print(c1.name)
print(c1.price)
c1.start_car(256)
c1.start_car(123)

