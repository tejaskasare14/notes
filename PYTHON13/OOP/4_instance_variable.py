class Demo:
    def im_instance_method(self):
       self.a = 30  #creating instance variable in instance method using self
       self.b = 40  #creating instance variable in instance method using self
       print("getting value of d from constructor",self.d) #accessing insiance variable
       self.d = 69852 #updating insiance variable
       print("after updating value of d from constructor",self.d)
       del self.d #deleting insiance variable
       #print("after deleting value of d from constructor",self.d) ERROR
       
    def __init__(self):
       self.c = 11  #creating instance variable in constructor using self
       self.d = 22  #creating instance variable in constructor using self
       
       
d1 = Demo()
d1.e = 5  #creating instance variable in outside a class using reference variable
# you will get error for a and b since im_instance_method() is not called yet
# print(d1.a)
# print(d1.b)
print(d1.c)
print(d1.d)
print(d1.e)

d1.im_instance_method()
print(d1.a)
print(d1.b)