class Person:
   def walking(self):
      print("self reference is :",id(self))
      print("person is waling")
      
p1 = Person()
print("p1 reference is :",id(p1))
p1.walking()

p2 = Person()
print("p2 reference is :",id(p2))
p2.walking()