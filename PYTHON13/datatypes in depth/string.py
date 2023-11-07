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

# index -> position od character in a string
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


#Operators on string
#operations on string