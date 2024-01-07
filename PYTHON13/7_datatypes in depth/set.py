#set example 
data = {10,"hi",5.3,10} 
#while creating a set you can add duplicate elemets but, 
# after runnning a code, you will get only unique elements


# ---------------- set properties -----------------
# duplicate not allowed
# hetrogeneous
# in {}
# mutable
# indexing not allowed
# insertaion order not preserved

# ---------------- how to crerate a set -----------------
# empty set
set1 = {} #this is not set, this is dict (disctionry)
print(set1)
print(type(set1))

#correct way of creating empty set use set() function
set2 = set() #this is set,
print(set2)
print(type(set2))

# form string to set using set(variable) function
s1="hello"
set3 = set(s1)
print(set3)
print(type(set3)) 


# from range() to set()
set3 = set(range(1,6))
print(set3)
print(type(set3))

# if we know the elemets
set4 = {10,23.6,10,25}
print(set4)


# operators on set
set5 = {1,2,3}
set6 = {11,22,33,3}

# set7 = set5+set6   #ERROR 
#print(set7) 

#print(set5*3) 

print(10 in set5)
print(10 not in set5)

# accessing set elements
# we cant access set emlemets since indexing is not allowed
set8 = {44,55,66,77,88,99}
#print(set8[0]) ERROR since indexing is not allowed


# operations on set
# Basic
print("----operations on set-----")
set9 = {33,44,55,66,44}
print(len(set9))
# print(set9.count(44)) #ERROR

# Adding elemets in set : we can add elemets in set but we cant tell their position
print("----- Adding elemets in set ----")
set10 = {1,2,3,4,5}
set11 = {11,22,33,44,55}

print(set10)
set10.add(8)
print(set10)

set10.update("hihi")
print(set10)

set10.update([100,200])
print(set10)

set10.update((1000,2000))
print(set10)

set10.update(set11)
print(set10)


# removing elemets from set
print("----- removing elemets from set ----")
set12 = {11,22,33,44,55,66,77,88}
print(set12)

set12.pop() # pop() -> removes any elemet from set
print(set12)

set12.remove(22) #remove -> remove given element from set, if elemet not present, then it will gives erro. check below
print(set12)
#set12.remove(222) #ERROR coz, 222 is not in set
set12.discard(222) #NO ERROR
print("after discarding 222 from set12 : ",set12)

set12.clear()  #removes all elemets 
print(set12)





# set comprehension -> creating a set. shortcut to create a set
# print("---- set comprehension----------")
# syntax : [ expression  for  condition]
set13 = {10,25,36,45,86,26}
print(set13)
even_set = {num   for num in set13   if(num%2==0)}
print(even_set)

greater_than_40 = {num   for num in set13   if(num>40)}
print(greater_than_40)


#find number greater than 40 which are even from set13
data = {num   for num in set13   if(num>40 and num%2==0)}
print(data)


# set operations

set1 = {1,2,3}
set2 = {3,4,5}

#union : return common elemets after eleminating duplicates 
print(set1.union(set2)) 

#intersection : return common elemets from both sets\
print(set1.intersection(set2))

#difference : return unique elemets from left side set
print(set1.difference(set2))


#symmetric_difference : return unique elemets from both set
print(set1.symmetric_difference(set2))


#shallow VS deep copy
mySet = {10,20,30}
duplicate_set_mySet = mySet
print(mySet)
print(duplicate_set_mySet)

duplicate_set_mySet.add(40)
print(duplicate_set_mySet)
print(mySet)
print(duplicate_set_mySet is mySet)


print("----- shallow copy --------")
shallow_copy_mySet = mySet.copy()
print(mySet)
print(shallow_copy_mySet)
shallow_copy_mySet.add(50)
print("after adding 50")
print(mySet)
print(shallow_copy_mySet)

