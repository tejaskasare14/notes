# local variable : the variables inside a function
# global variable : the variable outside a function

age = 30 # global
def local_and_global():
   name = "raj" #local
   age = 25 #local 
   print(name)
   print(age)#here we are accessing local variable
local_and_global()
print(age)#here we are accessing global variable

#why we need global keyword :
# to create global variable inside a function
def global_inside_function():
   global city
   city="pune"
   print(city)
global_inside_function()
print(city)

# to update global variable inside a function
sum = 0 #global
def update_global_variable():
   global sum
   sum = 10#here we are updating global variable sum
   print(sum)
   
   
print(sum) #output : 
update_global_variable()
print(sum)
