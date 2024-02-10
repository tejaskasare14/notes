#operators : are tools/symbols that we use to perform operations on data
#ACALIMB : All Cricketers Are Lived In Mum-Bai

#Arithmatic  :+, -, *, /, %, //, **
#Comparision :<, >, <=, >=, !=, ==
#Assignment  :=, +=, -=, *=, /=.....
#Logical     :and, or, not
#Identity    :is, is  not
#Membership  :in, not in
#Bitwise     :&, |, ^, <<, >>, ~

#Arithmatic  :+, -, *, /, %(modulas/mod), //(floor division), **(exponenet/power)
print(10+2)
print(10-2)
print(10*2)
print(10/2) # in python division always gives floating point answer
print(10.0/2)
print(10%2) # % gives reminder so, the answer is zero
print(10%3) #1
print(10//2) #floor divison gives answer of division to lowest int
print(10//3) #3
#first 10/3 = 3.3333 then it will find lowest int from 3.33333 that is 3
print(12//5) #2
print(-10//3) #-4
print(10**2)

print(True+True) #in python, True consider as 1 and False as 0

#Comparision :<, >, <=, >=, !=, ==
#it retuns bool as result of comparision
print(10>2)
print(10<2)
print(10>=2)
print(10<=2)
print(10!=2)
print(10==2)

#Assignment  :=, +=, -=, *=, /=.....
#used to assign value to variable
x = 10
print(x)
x = x+5 #x=10+5 => 15
print(x)
x-=10 #x=x-10 => 15-10 => 5
print(x)
x*=5
print(x)

#Logical     :and, or, not
# and : return True if both conditions are True
#       and always go behind false
# or : return True if at least one condition is True
#      or always go behind true
# not : reverse the result
print(10>2 and 10>6)
print(10<2 and 10>6)

print(10>2 or 10>6)
print(10<2 or 10>6)

print(not 10>2)

#Identity    :is, is  not
# use for comparison of id/identity/virtual location/address of a variable
# int reusability -5 to 256
# we can reuse string object
# we cant reuse float or complex
a = 10
print(id(a))
b = 10
print(id(b))
print(a is b)
print(a is not b)

#Membership  :in, not in
#to check given value present in given collection
name = "prasad"
print("d" in name)
print("pra" in name)
print("sadd" in name)
print("sadd" not in name)

#Bitwise     :&, |, ^, <<, >>, ~
# & : and - set bit to 1 if both bits are 1
# | : or -  set bit to 1 if atleast one bit 1
# ^ : xor - set bit to 1 if both bits are different
# binary of 6 = 0000 0110
# binary of 7 = 0000 0111

#   0 0 0 0 0 1 1 0
#   0 0 0 0 0 1 1 1
# ------------------
#&  0 0 0 0 0 1 1 0   ==> 6
#|  0 0 0 0 0 1 1 1   ==> 7
#^  0 0 0 0 0 0 0 1   ==> 1
print(6&7)
print(6|7)
print(6^7)
print(6<<2) #shift bits to the left by 2
print(7>>2) #shift bits to the right by 2
# shortcut for not operator ~ ex : ~x = (-x-1)
print(~9) #(-9-1) = -10
print(~7) #(-7-1) = -8