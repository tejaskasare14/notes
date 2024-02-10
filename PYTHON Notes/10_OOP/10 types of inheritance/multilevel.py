class GrandParent:
   zamin = "200 acre"
   gold = "20 kg"

class Parent(GrandParent):
   money = 60000
   bike = "suzuki" 
   def diabetes(self):
      print("i have diabetes")
   
class Child(Parent):
   pass

c  = Child()
print(c.zamin)
print(c.money)