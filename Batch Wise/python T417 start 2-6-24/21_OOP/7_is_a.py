class X:
   my_bike = "KTM"
   my_car = "Honda"
   
class Thakur(X): #X IS-A parent of Thakur 
   pass

t = Thakur()
print(t.my_bike)
print(t.my_car)