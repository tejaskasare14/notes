#what is set
s1 = {10,20,"hello"}
#set is a collection of heterogenous unique elements inside {}

s2 = {10,20,10,30} #there is no problem
print(s2) #here 10 will be eliminated

#set properties
#1. different data type
#2. indexing not allowed
#3. no limit on size
#4. duplicate elments not allowed
#5. in {}
#6. mutable : we can perform chnages inside set like, add remove elements etc

#how to create set
#empty set 
s2 = {} #dict
print(type(s2))
s3 = set()
print(type(s3))
print(s3) #set()


#from string, list and tuple
s1="hello"
set1 = set(s1)
print(set1)

l1=[10,30,10,30,20]
set2 = set(l1)
print(set2)

t1=(10,30,"byee",30,20)
set3 = set(t1)
print(set3)

#from range()
set4 = set(range(1,6))
print(set4)
#if elements known already
s2 = {10,20,10,30} #there is no problem
print(s2)


#operators on set
set5 = {10,20,10}
set6 = {20,30}
#set7 = set5*2 #ERROR
#print(set7)
#set8 = set5+set6 #ERROR
#print(set8)

print(10 in set5)
print(10 not in set5)

#accessing elements from set
s = {10,20,30,40}
#print(s[0]) ERROR

#set functions
#adding elements into set
#one elemenet at a time : add
set9 = {10,20}
set10 = {50,60,10}

print(set9)
set9.add(90)
print(set9)
set9.add("byee")
print(set9)


#mutiple elemenets (collection) at a time : update()
set9 = {10,20}
set10 = {50,60,10}
set9.update(set10)
print(set9)

set9.update("zoozoo")
print(set9)

#removing  elements from set
set12 = {11,55,33,66,22}
print(set12)

set12.remove(33)
#set12.remove(99)
print(set12)

set12.pop()
print(set12)

set12.clear()
print(set12)

#set 
set1 = {1,2,3}
set2 = {3,4,5}
#union :  returns all elements by removing duplicates
print(set1.union(set2))

#intersection :  returns common elemets in given set
print(set1.intersection(set2))

#difference :  returns all unique elements from left set
print(set1.difference(set2))

#symmetric_difference :  returns all unique elements from both set
print(set1.symmetric_difference(set2))