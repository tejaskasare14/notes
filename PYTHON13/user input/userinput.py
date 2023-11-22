#take input from user and display their sum
#default datatype given by input() function is string 
n1 = input("enter 1st number :") #10
n2 = input("enter 2nd number :") #20
print(type(n1))
print(type(n2))
result = n1+n2 #the result 1020 becuase default datatype is straing and if we use + on string, it perfroms concatination
print("addition is :", result) 


#solution : typecasting - way 1
x = input("enter 1st number :") 
y = input("enter 2nd number :") 
result = int(x) + int(y) # typecasting (data type changing)
print("addition is :", result) 

#solution : typecasting - way 2
s = int(input("enter 1st number :"))  # typecasting (data type changing)
t = int(input("enter 2nd number :") ) # typecasting (data type changing)
result = s + t 
print("addition is :", result) 


# addition of 2 numbers by diffrent type casting
p = int(input("enter 1st number :"))  # typecasting (data type changing into int)
q = float(input("enter 2nd number :") ) # typecasting (data type changing into float)
result = p + q 
print("addition is :", result)

# automatic type casting with input() function using eval() function

print("10+20+30") 
print(eval("10+20+30")) #evalues expression provided in quotes 
print(eval("10+20.5+30"))

p = eval(input("enter 1st number :"))  # automatically type casted based on provided value
q = eval(input("enter 2nd number :") ) # typecasting (data type changing into float)
print(type(p))
print(type(q))
result = p + q 
print("addition is :", result)


