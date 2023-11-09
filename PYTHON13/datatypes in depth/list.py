#lis example 
data = [10,"hi",5.3,10]
# ---------------- list properties -----------------
# duplicate allowed
# hetrogeneous
# in []
# mutable
# indexing
# insertaion order preserved

# ---------------- how to crerate a list -----------------
# empty list
list1 = []
print(list1)
print(type(list1))

#if we know emelents
list2 = [10,20,30]
print(list2)
print(type(list2))

#form string to list using list(variable) function
s1="hello"
list3 = list(s1)
print(list3)
print(type(list3))

#from split() to list
s2="9-11-2023"
list4 = s2.split("-")
print(list4)
print(type(list4))

#from range() to list()
list5 = list(range(1,6))
print(list5)
print(type(list5))


#operators on list
list5 = [1,2,3]
list6 = [11,22,33]

list7 = list5+list6
print(list7) #[1, 2, 3, 11, 22, 33] 

print(list5*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

print(10 in list5)
print(10 not in list5)

#accessing list elements
#either by using indexing or slicing
print("------accessing list elements--------")
list8 = [44,55,66,77,88,99]
print(list8[0])
print(list8[-1])
#print(list8[12]) list index out of range

print(list8[0:3], list8[:3]) #[44,55,66]
print(list8[4:6], list8[4:]) #[88,99]
print(list8[0:5:2])

#operations on list
#Basic
print("----operations on list-----")
list9 = [33,44,55,66,44]
print(len(list9))
print(list9.count(44))
print(list9.index(33))
print(list9.index(44))
#print(list9.index(444)) ERROR
#print(list9.rindex(44)) there is no rindex on list. it is only available for string

#Adding elemets in list
print("----- Adding elemets in list ----")
list10 = [1,2,3,4,5]
list11 = [11,22,33,44,55]

print(list10) #[1, 2, 3, 4, 5]
list10[0]=100
print(list10) #[100, 2, 3, 4, 5] data loss, sicnce 1 is not present

list10.append(9) #append -> add elemet at the end
print(list10)

list10.insert(0,1) #insert -> add elemet at the given index
print(list10)

list10.insert(50,8)  #if we try to add element at index larger than max index of given list, then element will be added at the end
print(list10)
print(list10.index(8))

list10.insert(-1,88)  #if we try to add element at index larger than max index of given list, then element will be added at the end
print(list10)

list10.extend(list10) #add other collection (string,list,tuple,set..etc) into given list at the end
print(list10)

list10.extend("hi")
print(list10)

#removing elemets from list
print("----- removing elemets from list ----")
list12 = [11,22,33,44,55,66,77,88]
print(list12)
del list12[0]
print(list12)
#del list12[10] ERROR due to index

list12.remove(22) #remove -> delete given element from list
print(list12)
#list12.remove(222) #ERROR coz, 222 is not in list

list12.pop() # pop() -> removes last elemet from list
print(list12)

# [].pop() #IndexError: pop from empty list . we cant pop elemet from empty list
print(list12)
list12.pop(2) # pop(index) -> removes  elemet from list at given index
print(list12)

list12.clear()  #removes all elemets 
print(list12)

#reverse and sort
print("------ reverse and sort ------------")
list13 = [44,66,11,33,22]
print(list13)
list13.reverse()
print(list13)
list13.sort()
print(list13)
list13.sort(reverse=True)
print(list13)

#list comprehension -> creating a list. shortcut to create a list
print("---- list comprehension----------")
data = [1,2,4,3,7,8]

# find even numbers in given list
# solution 1-> without using list comp

even_nos =[]
for num in data:
   if num%2==0:
      even_nos.append(num)

print(data)
print(even_nos)

# solution 2-> with list comp
even_data = [ num  for num in data if(num%2==0)]
print(even_data)

# add 5 in each element in given list - data using list comp
adding_five = [num+5  for num in data]
print(adding_five)




