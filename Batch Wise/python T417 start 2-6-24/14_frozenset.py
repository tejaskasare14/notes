#what is frozenset
s1 = {10,20,"hello"}
#frozenset is a collection of heterogenous unique and immutable  elements inside frozenset({})

s2 = frozenset({10,20,10,30}) #there is no problem
print(s2) #here 10 will be eliminated

#frozenset properties
#1. different data type
#2. indexing not allowed
#3. no limit on size
#4. duplicate elments not allowed
#5. in {}
#6. immutable : we cant perform chnages inside frozenset like, add remove elements etc

#how to create frozenset
fs1 = frozenset({10,20,10,30})
print(fs1)

l1 = [10,20,30,"hello"]
t1 = (10,20,30,"hello")
s1 = "python"
set1 = {11,22,33}
fs2 = frozenset(l1)
fs3 = frozenset(t1)
fs4 = frozenset(s1)
fs5 = frozenset(set1)
print(fs2)
print(fs3)
print(fs4)
print(fs5)

#set operations on frozenset
fset1 = frozenset({1,2,3})
fset2 = frozenset({3,4,5})
#union :  returns all elements by removing duplicates
print(fset1.union(fset2))

#intersection :  returns common elemets in given set
print(fset1.intersection(fset2))

#difference :  returns all unique elements from left set
print(fset1.difference(fset2))

#symmetric_difference :  returns all unique elements from both set
print(fset1.symmetric_difference(fset2))