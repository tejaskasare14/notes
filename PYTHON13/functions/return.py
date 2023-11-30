def cal(x,y):
   add=x+y
   sub=x-y
   return add,sub #we can return multiple values at a time in python
result = cal(20,5)
print(result) #since we are returning multiple values, we will get tuple of values (25,15)
   