class Parent:
   paisa = 2000000
   gold = "50 kg"
   def marriage(self):
      print("you have to marry shubhlaxmi")
   
class Prashant(Parent):
   def marriage(self):
      print("i will marry shital")
      my_paisa = super().paisa + 3000000
      print(my_paisa)
      super().marriage()
p = Prashant()
print(p.paisa)
print(p.gold)
p.marriage()