#what is tuple
t1 = (11,12,11,"hello")
#tuple is a collection of heterogenous elements inside round brackets ()/ parenthesis

#tuple properties
#1. different data type
#2. indexing allowed
#3. no limit on size
#4. duplicate elments allowed
#5. in ()
#6. immutable : we cant perform chnages inside tuple like, add remove elements etc

#tuple VS list
#() - []
#immutable - mutable


#how to create tuple
#1. empty tuple
t1 = ()
print(type(t1))

#2. tuple with only one element
t2 = (12) #datatype is int
t3 = (15,)#datatype is tuple
print(type(t2))
print(type(t3))
x = 10,20
print(type(x))
#3. elements known
t4 = (10,20,44,"hello",10)

#4. from other data type
l1 = [10,20,30]
s1 = "bye"
l1_to_tuple = tuple(l1)
print(l1)
print(l1_to_tuple)
s1_to_tuple = tuple(s1)
print(s1)
print(s1_to_tuple)

#5. from range()
one_to_five_tuple = tuple(range(1,6))
print(one_to_five_tuple)

#operators on tuple
t5 = (11,22)
t6 = (33,44)
t7 = t5+t6
print(t7)

t8 = t5*2
print(t8)

print(33 in t5)
print(33 not in t5)

#adding or removing elements from tuple
#since tuple is immutable, we cant do modification in it.
t9 = (99,44,55)
#t9.append(66) #AttributeError: 'tuple' object has no attribute 'append'
#t9.clear() #AttributeError: 'tuple' object has no attribute 'clear'




#Accessing tuple elements - index,slicing,loop
t10 = (40,50,70,90,10)

print(t10[1])
#print(t10[8]) #IndexError: tuple index out of range

print(t10[2:4]) #(70,90)

for i in t10:
   print(i)

print("---while loop---")
index = 0
while(index<5):
   print(t10[index])
   index = index+1
   

#len,index,count,sorted,min,max
t11 = (10,50,60,30,50)
print(len(t11))
print(t11.index(50))
#print(t11.index(90))
print(t11.count(50))
print(t11.count(500))
print(min(t11))
print(max(t11))
print(sorted(t11)) #returns new list 
print(t11)
print(sorted(t11,reverse=True)) #returns new list 


#tuple packing and unpacking
t12 = 10,"hello",20.3 #packing of multiple values into one variable
print(t12)

v1,v2,v3 = t12 #unpacking of tuple into exact number of variables
print(v1)
print(v2)
print(v3)

#i1,i2 = t12 #ValueError: too many values to unpack (expected 2)

e1 = t12 #it wil work
print(e1)