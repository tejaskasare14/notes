#method overloading
#not supportted due to if we create 2 methods with same name then
#pervious one will be overridden by new one (line duplicate keys in dict)
class Test:
   x = 10
   x = 20
   def add(self,x,y):
      print(x,y)
   
   def add(self,a,b,c):
      print(a,b,c)
      
t = Test()
#t.add(10,20) #this will call add() of line 6 not line 3
t.add(10,20,30)


#method overridding 
#super() : is used to call parent class's members if child and parent class having 
# members (variable/methods) with same name
class Parent:
   paisa = "10 Cr"
   jamin  = "25 Acre"
   
   def marriage(self):
      print("you have to marry fulan devi")
   
   def test(self):
      print("i am test from parent")
   
class Pratham(Parent):
   paisa = "10 Rs"
   def marriage(self):
      print("i will marry janvi kapoor")
      #marriage() #if we do this, then this will e recusrsion
      super().marriage()
      print(super().paisa)
      self.test()
      

p = Pratham()
print(p.paisa)
print(p.jamin)
p.marriage()

