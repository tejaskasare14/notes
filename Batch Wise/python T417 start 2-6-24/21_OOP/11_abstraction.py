#abstraction : partial implemantation of class or method.
#abstract method : 
      # method with zero implemention "pass"
      #            AND
      # method having decorator @abstractmethod
      
#abstract class : 
      # class which is having at least abstract method
      #              AND
      # a class must be inherited from ABC class
      # abstract class can have non abstract method also

from abc import *     
class Vehicle(ABC):
   
   @abstractmethod
   def wheels(self):
      pass

   def mirros(self):
      print("vehicle has 2 mirros ")

class Car(Vehicle):
   def wheels(self):
      print("car has 4 wheels")
      
class Bike(Vehicle):
   def wheels(self):
      print("bike has 2 wheels")

c = Car()    
c.wheels()
c.mirros()

b = Bike()
b.wheels()
b.mirros()
