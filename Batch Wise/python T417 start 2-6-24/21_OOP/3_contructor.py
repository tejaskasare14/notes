class Employee:
   institute = "ITVedant" #institute is static variable : value same for all objects
   
   def __init__(self,name,age): #name,age are instance variable : value is changing from object to object
      self.ename = name
      self.eage = age
      print("hello contructor")
      
   def hello():
      print("hello python")
   
e1 = Employee("raj",30)
e2 = Employee("pratham",20)

print(e1.ename) #raj
print(e2.ename) #pratham
print(e1.institute)
print(e2.institute)