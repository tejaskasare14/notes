# Arithmatic : +,-,*,/,//,**,%
# List out all others

print(10+5)
print(10-5)
print(10*5)
print(10%2) #reminder 0
print(10**2)
print(10/5) #in python, division always get floating result
print(10.0/5)
print(10/3)

print(10//3) #3.33  => 3
print(5//2)  #2.5   => 2
print(10//5) #2
print(10.0//5) #2.0

print(-10//2)
print(-10//3)

print(True+True) #2, internally PVM consider True as 1 and False as 0

# perform all comparision operator ==> 



#assignment operator
print("----- assignment operator -----")
x = 10
print(x)
x = x+5
print(x)
x-=10
print(x)

#logical
print("----- logical operator -----")
# and => True if both conditions are True
print(10>5 and 10>2)
print(10<5 and 10>2)

# or => True if at least one condition is True
print(10>5 or 10>2)
print(10<5 or 10>2)

#not => reverse the result
print(not True)


#identity ==> use for address comarision
print("----- identity operator -----")
p = 20
q = 20
print(id(p))
print(id(q)) # reusabilty
print(p is q) #True
print(p is not q)  #False
q = 50
print(id(q)) # immutability
print(p is q)
print(p is not q)

#membership operator
print("----- membership operator -----")
name = "raj"
print('a' in name)
print('z' in name)
print('z' not in name)
marks =[98,95,96,98]
print(98 in marks)

#bitwise operator
print("----- bitwise operator -----")
print(12 & 6)
print(12 | 6)
print(12 ^ 6)
print(~6)
print(~135)
print(12>>3)
print(6<<2)

