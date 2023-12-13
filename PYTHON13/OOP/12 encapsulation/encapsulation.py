class Hr:
   __x = 10  #private variable
   _id = 1
   _monthly_salary = 10000
   _name = "raj"
   _leaves = 2
   def hiring(self):
      print("accessing __x inside HR class", self.__x)
      print("this months hiring = 5")
      
   def __offering_package(self): #private method
      print("I am non accessible")
      
class Accounts(Hr):
   def salry_prosessing(self):
      #print(self.__x) ERROR
      
      daily_salary = 10000/30
      salary  = self._monthly_salary - (daily_salary*self._leaves)
      print("salary for id ", self._id, "is", salary)
      
a = Accounts()
a.salry_prosessing()
# a.__offering_package() ERROR
a.hiring()
   