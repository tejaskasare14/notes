# to take input from user, we have to use input() function
# the deafult data type of input() function is string

#ex : take two numbers from user and print theri sum
x = input("Enter first number :")
y = input("Enter second number :")
print("datatype of x is :", type(x))
print("datatype of y is :", type(y))
print(x+y) #here you will get concanited (join) output

# solution  : type casting - change data type from one to another
# to change into int use       => int(n)
# to change into float use     => float(n)
# to change into complex use   => complex(n)
# to change into str use       => str(n)

# way 1 of type casting while taking an input
x = input("Enter first number :")
y = input("Enter second number :")
x1 = int(x)
y1 = int(y)
print("datatype of x is :", type(x1))
print("datatype of y is :", type(y1))
print(x1+y1)

# way 2 of type casting while taking an input
x = int(input("Enter first number :"))
y = float(input("Enter second number :"))
print("datatype of x is :", type(x))
print("datatype of y is :", type(y))
print(x+y)

# way 3 of type casting while taking an input
x = eval(input("Enter first number :"))
y = eval(input("Enter second number :"))
print("datatype of x is :", type(x))
print("datatype of y is :", type(y))
print(x+y)

# another use of eval()
print(12+5+3)
print("12+5+3")
print(eval("12+5+3"))