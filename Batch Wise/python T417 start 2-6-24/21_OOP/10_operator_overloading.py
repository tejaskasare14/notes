class SimpleMath:
   def add(self,x,y):
      print(x+y)
      
   def __init__(self,a):
      self.x = a
      
   def __add__(self,other):
      return self.x + other.x
      
s = SimpleMath(5)
s.add(10,20)
s.add("hi","bye")
s1 = SimpleMath(200)
s2 = SimpleMath(300)
p = 20
q = 30
s.add(p,q)
s.add(s1,s2)
