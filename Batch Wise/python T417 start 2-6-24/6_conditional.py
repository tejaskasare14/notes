# why ? to perform some action based on condition
# if(condition), if(condition) else, if(condition) elif(condition)(n) else
# if is entry point and else is exit point

# check given number is even or odd
a = 105
if(a%2==0): #code inside if is execute only when the condition is True
   print(a, " is even")
else: #code inside else is execute only if condition is False
   print(a, " is odd")

#to check given no is +ve, -ve or zero
x = 25
if(x>0):
   print(x, " is positive")
elif(x<0):
   print(x, " is negative")
else:
   print(x, " is zero")
   
#take age from user and check wheter he/she is eligible for votting
#take number from user and check if that number is perfect square
n = 15
base_number = n**0.5
if(base_number**2 == n):
   print(n, "is perfect square")
else:
   print(n, " is not perfect square ")
#take number from user and check that number is 2 digit number

