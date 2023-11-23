#function without parameters
def add():    #add is a function name
   x=10
   y=20
   result = x+y
   print(result)

add()  #function call       
add()  #you can call function as many times you want
add()

#function with parameters
def sub(x,y):  # x and y are parameters : value requred for the funcion
   result1 = x-y
   print(result1)
   p = x
   q = y
   result2 = p-q
   print(result2)
sub(30,20)   #30,20 are argumets : value passed to the function
sub(40,20)   #40,20 are argumets : value passed to the function
#sub(50)      # TypeError: sub() missing 1 required positional argument: 'y'


# type of arguments
# 1. required arguments
# 2. positional arguments
# 3. keyword arguments
# 4. default arguments
# 5. variable length arguments


# 1. required arguments : those are compulsory reqired for the function
def req_arg(p,q):
   result = p+q
   print(result)
req_arg(10,20)
# req_arg(50) ERROR since 50 is assigned to p and thre is no value for q

# 2. positional arguments :   order of argument matters
def pos_arg(name,age):
   print("your name is ", name)
   print("your age is ",age)
pos_arg("raj",30)
pos_arg(40,"aniket") # position is compomised

# 3. keyword arguments : to overcome positional arguments. use parameter name while passing arguments
def key_arg(name,age):
   print("your name is ", name)
   print("your age is ",age)
key_arg(35,"rani") 
key_arg(age=35,name="rani")
#key_arg(age=35,"rani") keyword argument must be last. given below
key_arg("rani",age=35)

# 4. default arguments : when we dont pass argumnets, dafult value will be provied to parameter
# when we pass value to default argumnet, it will override defualt value
def def_arg(p,q=0): #here q is default argument
   result = p+q
   print(result)
def_arg(100,200)
#def_arg(100)
def_arg(100)


# 5. variable length arguments : only one paramter to multiple arguments
def sum(x,y):
   print(x+y)
sum(20,30)

def sum2(x,y,z):
   print(x+y+z)
sum2(20,30,40)

#sol
def summ(*data): # here, data will be converted into tuple
   print(data)
   sum = 0
   for n in data:
      sum+=n
   print(sum)
   
   data_into_list = list(data)
   print(data_into_list)
summ(40)
summ(40,50)
summ(40,50,60)


#mixing of all arguments
def test(a,b,c,d=0,e=0):
   print(a,b,c,d,e)
test(10,20,30,e=90,d=60)