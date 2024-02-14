#string : is colletion of numbers, alphabates or symbols enclosed withing 
#         single quote, double quotes or triple quotes
#why triple quotes? : to define multi line string in python, we use triple quotes

f = 'z'
g = 'python123$'
h = "java@@12"
i = "5646464"
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))
# we cant write multi line string using single or double quotes in python ex -
# k = "my name is tejas
# i live in thane"

j = """my name is tejas
      i live in thane"""
      
k = '''my name is tejas
       i live in thane'''

print(j, type(j))
print(k, type(k))

#string must be start and end with same quotes
# subject = "the subject is python'

#-----------------accessing string characters------------------------
name = "john"
print(len(name)) #we have total 4 chacters in name string

#to acces indivisaul character from string, we have to use "index"
#index - position of character in string
#python is always zero based index (always index start from zero)
# 0   1   2    3   ---> forward direction
# j   o   h    n
#-4  -3  -2   -1   <--- backward direction

#conclusion:
#every element present inside collection in python has 2 indices > +ve and -ve
#left most element has 0 index
#right most elemet has -1 index
name = "john"
print(name[0]) #who is at 0th index - j
print(name[-1]) #who is at -1th index n
#print(name[5]) #IndexError: string index out of range

#we can access all chacters at a time by using any loop
name = "john"
for charcter in name:
   print(charcter, end=" ")

print()

i = 0
while(i<len(name)):
   print(name[i],end=",")
   i+=1

#slice operator in string
#to get a part of a collection we need slice. check below name example
#slice : sub part of a string ex
name = "raj" #substring/slice: r, ra, aj, j
#syntax :
   #varible[start:end:step]
#step value is optinal 
#default step value is 1
#default start value is 0
#default end value is end of that string

name = "mahabharat"

# 0      1   2    3     4    5   6     7    8   9
# m      a   h    a     b    h   a     r    a   t
# -10   -9   -8   -7   -6   -5   -4   -3   -2   -1

name = "mahabharat"
print(name[0:len(name):1])
print(name[0:10:1])
print(name[::])
#slicing from begining
print(name[0:4], name[:4]) #maha
print(name[0:7], name[:7]) #mahabha
#slicing till end
print(name[8:10],name[8:])#at
print(name[4:10],name[4:])#bharat
#middle slicing
print(name[3:7]) #abha

#advanced slicing

# 0      1   2    3     4    5   6     7    8   9
# m      a   h    a     b    h   a     r    a   t
# -10   -9   -8   -7   -6   -5   -4   -3   -2   -1

name = "mahabharat"
#step_value = to_skip + 1
#to_skip = step_value-1
print(name[::2]) # start from 0 go till 10 by skipping 1
#step to solve problem
#step 1 - check sign of step value
#step 2 - based on sign descide slicing direction

#in above example the sign of step value is +ve so direction is L to R
# start from 0 go till 10 by skipping 1

name = "mahabharat"
print(name[5:9:-1])
#step sign is -ve so we have to go from R to L
#start from 5 and go to the left, here we will never get 9. so the answer is blank string
print(name[5:9:1])

print(name[9:2:-2])

#------------------OPERATORS ON STRING ----------------------
print("hi"*5)
print("hi"+"bye")

print("n" in "python")
print("n" not in "python")

print("a">"A") #char by char comparision baseed on ASCII code
#a = 97
#A = 65
print("raj">"bablu")#char by char comparision. r get comared with b
print("raj">"raju")

#-----------------------STRING FUNCIONS----------------------------
#changing case of a string
print("HeLLo".lower())
print("HeLLo".upper())
print("HeLLo".swapcase())
print("tejas kasare".title())
print("my name is tejas i live in delhi.".capitalize())
print("HELLO45".lower()) #NO ERROR

#checking case and content in a string
print("HELLO".isupper())
print("HeLLO".isupper())

print("hello".islower())
print("Hello".islower())

print("hello Python".istitle())
print("Hello Python".istitle())

print("hello".isalpha())
print("hello5".isalpha())

print("hello45".isalnum()) #character or number
print("hello".isalnum()) #True
print("1234".isalnum()) #True

print("45".isdigit()) #True
print("R45".isdigit()) #False

print("Tejas Kasare".isspace()) #False
print(" ".isspace()) #True