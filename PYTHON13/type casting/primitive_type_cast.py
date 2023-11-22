# primitive : int,float,complex,bool,str

# int - int(a)
# float - float(b)
# complex - complex(a,b)
# string - str(a)
# boolean - bool(a)

# tyepcast : converting one data type into another
# implicit : automatic type casting - lower to heighr data type
# explicit : manual type casting - higher to lower

a = 10

b = float(a)
print(b)

c = complex(a) #a+bj , here a and b are 2 numbers(can be int or float), since we are passing only one argument, it it considerd as a and b becomes zero
print(c)
d = complex(a,b)
print(d)
e = complex(50,26.3)
print(e)

f = str(a)
print(f)
print(type(f))

g = bool(a)
print(g)
#for bool, non zero numbers and non empty strings are true, all others false
print(bool(35))
print(bool(-12))
print(bool(0))
print(bool(0.0))
print(bool("hi"))
print(bool(" "))
print(bool(""))

# derived or colletion data type casting
# to convert into             built in function
#  list                 -     list()   
#  tuple                -     tuple()
#  set                  -     set()
#  frozenset            -     frozenset()
#  dictionary           -     dict()

list_data = [10,20,30,20]
tuple_data = tuple(list_data)
set_data = set(list_data)
frozenset_data =frozenset(list_data)

print(list_data)
print(tuple_data)
print(set_data)
print(frozenset_data)

