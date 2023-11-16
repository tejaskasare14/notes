#tuple example 
data = (10,"hi",5.3,10)
# ---------------- tuple properties -----------------
# duplicate allowed
# hetrogeneous
# in ()
# immutable
# indexing
# insertaion order not preserved (since tuple is immutable,we cant add elements in it)

# ---------------- how to crerate a tuple -----------------
# empty tuple
tuple1 = ()
print(tuple1)
print(type(tuple1))

#tuple with only one element
#tuple2 = (12.23) --> this tuple is not valid. if we check type then we eill get float becuase o 12.23
tuple2 = (12.23,)
print(tuple2)
print(type(tuple2))


#if we know emelents
tuple3 = (10,20,30)
print(tuple3)
print(type(tuple3))

tuple4 = 100,200,300
print(tuple4)
print(type(tuple4))



#form string to tuple using tuple(variable) function
s1="hello"
tuple5 = tuple(s1)
print(tuple5)
print(type(tuple5))

#form list to tuple using tuple(variable) function
mylist = [11,22,33]
print(mylist)
tuple6 = tuple(mylist)
print(tuple6)
print(type(tuple6))

#from range() to tuple()
tuple7 = tuple(range(1,6))
print(tuple7)
print(type(tuple7))


#operators on tuple
tuple8 = (1,2,3)
tuple9 = (11,22,33)

tuple10 = tuple8+tuple9
print(tuple10) #(1, 2, 3, 11, 22, 33)
print(tuple8)

print(tuple8*3) #(1, 2, 3, 1, 2, 3, 1, 2, 3)
print(tuple8)

print(10 in tuple8)
print(10 not in tuple8)

#accessing tuple elements
#either by using indexing or slicing
print("------accessing tuple elements--------")
tuple11 = (44,55,66,77,88,99)
print(tuple11[0])
print(tuple11[-1])
#print(tuple11[12]) #tuple index out of range

print(tuple11[0:3], tuple11[:3]) #[44,55,66]
print(tuple11[4:6], tuple11[4:]) #[88,99]
print(tuple11[0:5:2])

#operation on tuple

l1 = [10,20,30]
l1.append(40)
print(l1)

t1 = (100,200,300,100)
#t1.append(400) error
# we cant add or remove elemets from TUPLE

print(len(t1))
print(t1.index(100))
#print(t1.index(500))
print(t1.count(100))
print(sorted(t1))
print(sorted(t1,reverse=True))
print("min :",min(t1))
print("max :",max(t1))
print(min(("rajaaaaaaaaaaa","raju","z")))
print(max(("raj","raju","z")))
#print(max(("raj","raju",12,0)))  ERROR




# packing and unpacking of tuple

t1=10,20,30 #packing of tuple
print(t1)

a,b,c = t1  #UNPACKING OF TUPLE --> a=10,b=20,c=30
print(a)
print(b)
print(c)

# p,q,r,s,t = t1 # ERROR -> while unpcaking, values and varibales count must match\
# x,y = t1       # ERROR -> while unpcaking, values and varibales count must match\











