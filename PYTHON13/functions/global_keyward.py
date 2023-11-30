def add(x,y):
   name="raj" #here name is local varibale
   result = x+y #here result is local variable for function add. we cant access result variable outside a function
   print(result)
   
add(12,10)
#print(result) #name 'result' is not defined

# global keyword
# use 1 : declaring global variable inside function
def sub(x,y):
   global sub_result #declaring global variable inside function
   sub_result=x-y
   print(sub_result)
   
sub(20,5)
print("accessing sub_result outside a function :", sub_result)

# another use of global jeyword : to change already existing global varible's values inside a function
age = 30
def change_age():
   global age
   age = 40
   print("age inside a function :",age) #40
change_age()
print("age outside a function :",age) #40

#if name of local and global variable is same then  more priority given to local variable
city = "pune"
def hello():
   city="thane"
   print("city inside function: ",city) #more priority to local variable
hello()
print("city inside function: ",city) #more priority to global variable
