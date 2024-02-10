class Car:  #class
   name = "honda" #variable/propertie
   milage = 35    #variable/propertie
   
   def engine(self):  #method/behaviour
      #self is pointing towards currenct object
      print(self)
      print("Car is running")

Car()  #  object  -> this is useless object
c1 = Car() # c1 is reference variable, pointing to object Car()
print(c1.name)
print(c1.milage)
c1.engine() # when object is created, it brodcasts it reference and it is duty of every 
            # method present inside class to receive and store that refernce for future use
      