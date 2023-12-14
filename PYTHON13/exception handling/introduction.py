# in python following exceptions are avalibale

#ZeroDivisionError: division by zero
#print(10/0)

#NameError: name 'x' is not defined
#print(x)

#TypeError: can only concatenate str (not "int") to str
#print("hello"+5)

# IndexError: list index out of range
# data = [10,20,30]
# print(data[5])

# to handle this type of exceptions we have to use special type of code
# try : add risky code
# except(class Name) : add handling code
# finally : add resource de-allocation code

#example - without exception handling
# x = eval(input("enter first number:"))
# y = eval(input("enter second number:"))
# print(x/y)
# print("thank you")

#example - with exception handling
# x = eval(input("enter first number:"))
# y = eval(input("enter second number:"))
# try:
#    print(x/y)
#    print("I am after risky code")
# except: #this except is called as default except (why? becoz there is no any class name)
#    print("you cant divide any number by zero")
   
# print("thank you")

# we can write multiple except with one try block
# x = eval(input("enter first number:"))
# y = eval(input("enter second number:"))
# try:
#    print(x/y)
#    print(age)
#    print("I am after risky code")
# except ZeroDivisionError:
#    print("you cant divide any number by zero")
# except NameError:
#    print("there is no variable age")
   
# print("thank you") 

# deafult except
# x = eval(input("enter first number:"))
# y = eval(input("enter second number:"))
# try:
#    print(x/y)
#    #print(age)
#    print("hello"+5)
#    print("I am after risky code")
# except ZeroDivisionError:
#    print("you cant divide any number by zero")
# except NameError:
#    print("there is no variable age")
# except:
#    print("I am default except")
# print("thank you") 

   
# without default except
# x = eval(input("enter first number:"))
# y = eval(input("enter second number:"))
# try:
#    print(x/y)
#    #print(age)
#    print("hello"+5)
#    print("I am after risky code")
# except ZeroDivisionError:
#    print("you cant divide any number by zero")
# except NameError:
#    print("there is no variable age")
# print("thank you") 

#finally
x = eval(input("enter first number:"))
y = eval(input("enter second number:"))
try:
   print(x/y)
   #print(age)
   print("hello"+5)
   print("I am after risky code")
except ZeroDivisionError:
   print("you cant divide any number by zero")
except NameError:
   print("there is no variable age")
finally:
   print("i will execute in abmornal termination also")
print("thank you") 
