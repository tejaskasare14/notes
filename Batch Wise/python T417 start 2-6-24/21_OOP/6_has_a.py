class Siddiqui:
   my_bike = "KTM"
   my_car = "Honda"
   
class Thakur:
   #Thakur class HAS-A object of Siddiqui
   s = Siddiqui()
   sbike=s.my_bike
   scar=s.my_car

t = Thakur()
print(t.sbike)
print(t.scar)