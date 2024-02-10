# type casting : process of converting one data type to other
# in python we have function for each data type for type casting

# int()
# float()
# complex()
# bool()
# str()
# list()
# tuple()
# set()
# frozenset()
# dict()


print(int(12.5))
print(float(25))
print(complex(15)) #a+bj, here 15 will be considerd as a and b became zero
print(complex(13.6,25)) #a+bj, here 13.6 will be considerd as a and b will be 25

# bool() returns false for 0,0.0 and ""
print(bool(35))
print(bool(-35))
print(bool(0))
print(bool(0.0))
print(bool("hello"))
print(bool("    "))
print(bool(""))

# str()
print(str(253.145))

# list()
print(list((12,23)))

# tuple()
print(tuple([12,23]))

# set()
print(set([12,23,12,45]))

# frozenset()
print(frozenset([12,23,12,45]))

# dict()
print(dict( ( (1,"raj"), (2,"rani") ) ))