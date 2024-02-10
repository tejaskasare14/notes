class Parent:
   money = 60000
   bike = "suzuki" 
   def diabetes(self):
      print("i have diabetes")
   
class Child(Parent):
   pass

c = Child()
print(c.money)
print(c.bike)
c.diabetes()