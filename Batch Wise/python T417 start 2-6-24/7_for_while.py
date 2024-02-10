#we use loop to iterate over given collection
#for loop : when we know the end ex: print numbr between 1 to 10
#while loop: when we dont know the end ex : please entre your password

#rule for loop : there must be 3 things in any loop
#1. intialize
#2. condition
#3. inc/dec

#working of range() function
#syntax : range(start,end,step_value) here step value is optinal
print(range(1,5)) #range(1,5)
print(list(range(1,5))) #[1, 2, 3, 4]
#it will start from 1 and goes till 4
#in range() end is always excluded




#we can use range with step value
#step_value = to_be_skip + 1
print(list(range(1,10,2))) #[1, 3, 5, 7, 9]
#in above example, step value is 2, so we have to skip 1 number

print(list(range(1,10,3))) #[1, 4, 7]
#in above example, step value is 3, so we have to skip 2 numbers

#create list of even numbrs between 2 to 10(inc)
print(list(range(2,11,2)))

#for loop
#for(i in collection) 
#print all numbers between 1 to 5(included)
for i in range(1,6):
   #here 1 comes from range and get stored temp inside i
   #for next interation 2 comes from range and get stored temp inside i
   #it get continues till 4 
   print(i)
   
#print even numbers between 1 to 10
for i in range(2,11,2):
   print(i)
   
