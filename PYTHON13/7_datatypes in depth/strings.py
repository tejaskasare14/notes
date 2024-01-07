#Introduction
# -> collection of characters inside single,double or triple quotes
a = 'x'
b = "hello"
#c = "gfivivoyfwipvytvwe
#     sdgsdgsdgsdg"  ERROR
# we cant write multi line string in double quotes so we have triple quotes

d = ''' Hello
       I am Python multi line string'''
       
e = """Hello
       I am Python multi line string"""
       
print(type(a))
print(type(b))
print(type(d))
print(type(e))

#importnat 
#f = "Hello python' ERROR
#string must start and end with same quotes
#g = "My name is "Tejas" "


g = "My name is 'Tejas' " #My name is 'Tejas'
f = 'My name is "Tejas" '
print(g)
print(f)

h = " python 121* %$@!8~f"
print(type(h))

# Accessing String elements/characters

# index -> position of character in a string
# index has two types -> positive and negative
# positive index -> starts from zero (Left to Right)
# negative index -> starts from -1 (Right to Left)
s="python"

#  0   1   2   3   4   5
#  p   y   t   h   o   n
# -6  -5  -4  -3  -2  -1
print(s[0])
print(s[-6])
#print(s[8]) #IndexError: string index out of range
#print(s[-10]) #IndexError: string index out of range

#Slice -> subpart/substring
#variable[start : end : step]
s = "python"

#py,pyh,p,pytho.... -> starts from zeroth index -> s[0:2] -> s[:2] -> py
#on,thon,n......... -> ends on last index       -> s[4:6] -> s[4:] -> on
#th,tho,yt......... -> middle index             -> s[2:4] -> s[2:4] ->th

#Advanced slicing
print("------ Advanced slicing -----------")
#1. working with step value
s="python"

#  0   1   2   3   4   5
#  p   y   t   h   o   n
# -6  -5  -4  -3  -2  -1

print(s[0:6:2])
# step value = to be skip + 1 
# skip = step value -1

# step 1 - check sign of step value -> +ve -> slicing is from L to R
# step 2 - starts with 0th index (for above example)
# step 3 - our step value (for above example) is 2 so we have to skip 1 elemet/character
# output -> 0->p      2->t     4->0

s = "maharashtra"
print(s[2:8:2])
print(s[2:-4:2])
print(s[-5:1:3])
print(s[6:1:-1])
print(s[::-1])

#Operators on string
print("---- Operators on string ------")
print("hello" + "bye")
print("hello" * 3)

print("z" in "zebra")
print("x" not in "zebra")

print("rajesh" > "raju") # 'e' > 'u'   --> character by character comparision (ASCII value)
print('a' > 'A')  #a ASSCII value -> 97 and A ASCII value 65
 
#operations on string
print(" ------  operations on string ---------------")
#changing case
s = "hello"
print("hello".upper())
print(s.upper())
print("HEllo".lower())
print("HELLO45".lower()) #no error -> only alphabates converted
print("tejas kasare".title())
print("HELlo".swapcase())
print("mango is seasonal fruit.apple is good.".capitalize())

#index of character
s= "python python"
print(s.index('p')) #first occurance
print(s.rindex('p')) #last occuarance
#print(s.index('z')) #Error
print(s.find('p'))
print(s.rfind('p'))
print(s.find('z'))  #-1 no error

#checking string content
print("---- checking string content-------")
print("pythonPython".isalpha())
print("python Python".isalpha())
print("pythonPython45".isalpha())

print("Hello45".isalnum())
print("Hello 45".isalnum())

print("hello".islower())
print("Hello".isupper())
print("HELLO".isupper())

print("454556".isdigit())

#counting characters in string
print("hello".count("l"))
print("hello".count("z"))
print(len("hello"))

#split and join
date = "8-11-2023"
splited_date=date.split("-") #Return a list of the substrings in the string, using sep as the separator string.
print(date)
print(splited_date)

joined_date="/".join(splited_date) #Concatenate any number of strings.
print(joined_date)

print(ord('a')) # to check ascii value

#checking start and end of a string
s = "python"
print(s.startswith("p"))
print(s.startswith("py"))
print(s.startswith("y"))

print(s.endswith("on"))

#replacing string character(s)
s="python"
s="pythom"
print("python".replace("n","m"))
name="raj"
replaced_name=name.replace("r","b")
print(name)
print(replaced_name)

#removing space
s1 = "        python"
print(s1)
print(s1.lstrip())

s2 = "python           "
print(len(s2))
print(len(s2.rstrip()))

s3 = "    python     "
print(s3)
print(s3.strip())

#loop on string
s="python"

for char in s:
       print(char)
       #print(char,end=" - ")

#find total vowels in given string -> a,e,i,o,u
s="hello"
#expected output -> 2
count = 0
for char in s:
       if(char in "aeiou"):
              count+=1
       else:
              pass
print(count)

#print total upper case characters in given string
s = "HELLopython"
#expected output -> 4
count = 0
for char in s:
       if(char.isupper()):
              count+=1
       else:
              pass
print(count)

#find occurance of each character
s = "honululu"
#h-1
#o-1
#n-1
#u-3
#l-2



















#more string function
s="python"






