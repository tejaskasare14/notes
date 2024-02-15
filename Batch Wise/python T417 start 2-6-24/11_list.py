#what is list
#list is collection of heterogeneous elements inside [] (square brackets).
# ex : data = [15,23.0,"hello",15]

# list properties

#1. different data type
#2. indexing allowed
#3. no limit on size
#4. duplicate elments allowed
#5. in []
#6. mutable

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
















# accessing list elements
# functions on list