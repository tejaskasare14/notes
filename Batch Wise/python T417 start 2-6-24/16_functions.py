#function : 
#  1. is set of code, which use to eleminate duplication of logic
#  2. and executes only when we call it 
#  3. we call a function as many times we want

def add(): #function defination
   a = 10
   b = 20
   result = a+b
   print(result)
add() #function call
add() #function call
add() #function call

#function with parametrs
def sub(a,b): #values required for a function - parametrs
   result = a-b
   print(result)
sub(10,2) #values that we pass while calling a function - arguments
sub(50,66)

#type of arguments
# 1. required aruments
# 2. positional aruments
# 3. keyword aruments
# 4. default aruments
# 5. variable length aruments


# 1. required aruments
def req_arg(x,y):
   result = x+y
   print(result)
req_arg(10,5)
#req_arg(15) #TypeError: req_arg() missing 1 required positional argument: 'y'

# 2. positional aruments
def pos_arg(name,age):
   print("my name is ", name)
   print("my age is ",age)
   
pos_arg("tejas",28)
pos_arg(28,"tejas") #position of an argument must match with parameter

# 3. keyword aruments : solution for positional arguments
def key_arg(name,age):
   print("my name is ", name)
   print("my age is ",age) 
key_arg("rani",30)
key_arg(age=30,name="rani")

# 4. default aruments : solution for required argument
def def_arg(x,y=0):
   result = x+y
   print(result)
def_arg(10,5)
def_arg(13)



# 5. variable length aruments
def var_len_arg(*n):
   print(n)
   print(type(type(n)))

var_len_arg(20,36,20)
var_len_arg(20,36,12)

x = 200,360
print(x)


