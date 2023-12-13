from abc import ABC, abstractmethod


#following class is not abstract class even there is abstract method in it . why?
# because Vehicle class must be child of ABC class

# class Vehicle:
#    @abstractmethod
#    def wheels(self):
#       pass
     
# v = Vehicle() 

#since Vehicle is not abstract class, we can create its object
# ---------------------------------------------------------------------------------
# following Vehicle class is abstarct class
# class Vehicle(ABC):
#    @abstractmethod
#    def wheels(self):
#       pass
   
# v = Vehicle() 

#since Vehicle is abstract class, we cant create its object

#---------------------------------------------------------------------------------

# abstract class can have non abstract method also
# class Vehicle(ABC):
#    @abstractmethod
#    def wheels(self):
#       pass
   
#    def mirrors(self):
#       print("vehicle has 2 mirrors")

# class Car(Vehicle):
#    pass

# honda = Car()

class Vehicle(ABC):
   @abstractmethod
   def wheels(self):
      pass
   
   def mirrors(self):
      print("vehicle has 2 mirrors")

class Car(Vehicle):
   def wheels(self):
      print("car has 4 wheels")

honda = Car()
honda.wheels()
   