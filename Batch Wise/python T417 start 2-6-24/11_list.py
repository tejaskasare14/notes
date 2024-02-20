#what is list
#list is collection of heterogeneous elements inside [] (square brackets).
# ex : data = [15,23.0,"hello",15]

# list properties

#1. different data type
#2. indexing allowed
#3. no limit on size
#4. duplicate elments allowed
#5. in []
#6. mutable : we can perform chnages inside list like, add remove elements etc

# how to create a list
#1. if elements are alredy known
data1 = [10,20,30]
print(data1)
#2. split function
data2 = "15-02-2024".split("-")
print(data2)
#3. empty list
data3 = []
print(data3)
#4. from other collection
data4 = list("hello")
print(data4)
#5. from range funtion
data5 = list(range(1,5))
print(data5)

# operators on list

l1 = [10,20]
l2 = [30,40]
l3 = l1+l2
print(l3) #[10, 20, 30, 40]
#l4 = l1*l2 ERROR
l5 = l1*3 
print(l5) #[10, 20, 10, 20, 10, 20]
print(10 in l1)
print(100 not in l1)


# accessing list elements : we can access by using index or sclicing
data = [55,88,22,44,33,99,77,22]
print(data)
print(data[1])
print(data[0:3], data[:3]) #[55,88,22]
print(data[5:8], data[5:]) # [99, 77, 22]
print(data[3:8:2], data[3::2]) # [44, 99, 22]


# functions on list
# find index of last occurance of 22 in given list
data = [55,88,22,44,33,99,77,22]
print(data.index(22))
#print(data.index(11)) #ValueError: 11 is not in list
print(data.count(22))

#adding elements in the list
data = [44,66,33]
print(data)
data.append(11) #add at the end
print(data) #[44, 66, 33, 11]
data.insert(0,99)
print(data) #[99, 44, 66, 33, 11]
data.insert(6,55)  #NO ERROR
#if we give index which is higher than max index of a list then it will add at the end
print(data)

names = ["raj","rani"]
data.extend(names) 
print(data) #[99, 44, 66, 33, 11, 55, 'raj', 'rani']
city = "pune"
#[99, 44, 66, 33, 11, 55, 'raj', 'rani']
data.append(city) # [99, 44, 66, 33, 11, 55, 'raj', 'rani', 'pune']
print(data)
data.extend(city) # [99, 44, 66, 33, 11, 55, 'raj', 'rani', 'pune', 'p', 'u', 'n', 'e']
print(data)

#removing element from list
data = [22,55,77,88,22,11]
print(data)
data.remove(22) #removes first occurance 
print(data) #[55,77,88,22,11]
#data.remove(33) #ValueError: list.remove(x): x not in list
print(data)
data.pop() #removes last element 
print(data) #[55,77,88,22]
data.pop(0) #removes elemet at given index
print(data) #[77, 88, 22]
#data.pop(5) #ERROR IndexError: pop index out of range
data.clear() #removes all lements from list
print(data)  #[]

#reverse and sort
data= [22,33,44,11,99]
data.reverse()
print(data)
data.sort()
print(data)
data.sort(reverse=True)
print(data)

#list comprehension : creating a list
#[expression forloop condition]
#while coding, write for loop first then codition and finally expression
#find even numbers in given list and add 5 in it
data = [22,33,44,55,11,66]
even_nums=[]
for num in data:
   if(num%2==0):
      even_nums.append(num+5)     
print(even_nums)

even_list = [i+5 for i in data if(i%2==0)]
print(even_list)

