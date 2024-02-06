# datatype is used to recognize what kind of data variable holds.

# in python, datatype is categorise into 3 parts: numeric, boolean and collection
# in python, there is no limit on data

# in numeric there are 3 data types :int, float and complex
# in booelan there is one datatype : bool/boolean
# in collection there are 6 datatypes: string,list,tuple,set,frozenset and dictionary

# Numeric data type
#int : whole numbers
#float: decimal numbers
#complex: the number which is written in the form of a+bj 
#         where a and b can be int or float and j is imagenery number
#         j = under root -1


a = 10
b = 10.5
c = 10+12.3j

print(a, type(a)) #type() is used to check data type of a variable
print(b, type(b))
print(c, type(c))

#boolean : used to store yes-no type value. it has only 2 values True & False
d = True
e = False

print(d,type(d))
print(e,type(e))

#collection : used to store multiple values in single variable
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

#list
#tuple
#set
#frozen set
#dictionary
      
m = [10,20,"hello",10]
n = (10,20,"hello",10)
p = {10,20,"hello",10}
q = frozenset({10,20,"hello",10})
r = {'name':'raj','age':25}
print(m, type(m))
print(n, type(n))
print(p, type(p))
print(q, type(q))
print(r, type(r))
