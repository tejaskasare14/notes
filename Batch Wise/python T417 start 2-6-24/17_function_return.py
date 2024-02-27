def add(x,y):
   result = x+y
   print(result)
add(10,20)
#print(result) #NameError: name 'result' is not defined
#the variables present inside a function are called as local variable
#and we cant access local variables outside of a function body
#since result local variable we cant access outiside of a function\
   
#still, if you want to access the local variable outside of funtion then there 
#are 2 ways : return that variable or ma

#generally we use return to access final output of  a function, outisde of a function
#when we return a value it goes to the function call
#if your function is returning a value then store its function call into a varibale (see line 27 below)



def sub(a,b):
   result  = a-b
   #i want to access result ouside of function the return the result
   return result #5

sub(10,5)
print(sub(20,6))
print(sub(20,6))
output = sub(50,30)
print(output)
print(output)
print(output)



#we can return multiple values at time in python
def calci(p,q):
   add = p+q
   sub = p-q
   div = p/q
   return add,sub,div

result=calci(10,2)
print(result)
