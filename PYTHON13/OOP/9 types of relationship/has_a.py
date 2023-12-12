class Amit:
   money = 50000
   bike = "honda"
   
class Prashant:
   #we have to create object of Amit in order access money
   #because : amit HAS-A money
   amit_obj = Amit()
   p_money = amit_obj.money-20000
   #now we can say , Prashant HAS-A object of Amit
   
prashant_obj = Prashant()
print(prashant_obj.p_money)