#we use loop to iterate over given collection
#for loop : when we know the end ex: print numbr between 1 to 10
#while loop: when we dont know the end ex : please entre your password

#rule for loop : there must be 3 things in any loop
#1. intialize : to start the lopp
#2. condition : to terminate the loop
#3. inc/dec

#working of range() function
#syntax : range(start,end,step_value) here step value is optinal
print(range(1,5)) #range(1,5)
print(list(range(1,5))) #[1, 2, 3, 4]
#it will start from 1 and goes till 4
#in range() end is always end-1


#we can use range with step value
#step_value = to_be_skip - 1
print(list(range(1,10,2))) #[1, 3, 5, 7, 9]
#in above example, step value is 2, so we have to skip 1 number

print(list(range(1,10,3))) #[1, 4, 7]
#in above example, step value is 3, so we have to skip 2 numbers

#create list of even numbrs between 2 to 10(inc)
print(list(range(2,11,2)))

#for loop
#syntax : for(i in collection) here i is any temp variable
#print all numbers between 1 to 5(included)
for i in range(1,6):
   #here 1 comes from range and get stored temp inside i
   #for next interation 2 comes from range and get stored temp inside i
   #it get continues till 4 
   print(i)
   
#print even numbers between 1 to 10
for i in range(2,11,2):
   print(i)
   
#print even numbers between 1 to 10
for i in range(1,11):
   if(i%2==0): #1%2==0, 2%2==0, 3%2==0, 4%2==0, 5%2==0, 6%2==0, 7%2==0, 8%2==0, 9%2==0, 10%2==0
      print(i) #2 4 6 8 10
      
#prin all characters in give string "hanuman"
s = "hanuman"
for character in s:
   print(character)
   
#print all numbers in given list
marks = [99,95,96,92,12]
for mark in marks:
   print(mark)
   
#print even and odd numbers from below list
prices = [99,48,63,92,50]
for price in prices: #for each price present inside prices
   if(price%2==0):
      print(price, " is even")
   else:
      print(price, " is odd")
      
#print only 2 digit numbers from give list
numbers = [235,12,41,236,251,22]
#expected output : 12 41 22
for number in numbers:
   if(number>9 and number<100):
      print(number," is two digit")

# ---------------------WHILE LOOP------------------------------

#while(condition):
#  code

# exxecutes until condition is true
number = 45
guess = 0  #initilization
while(guess!=number): #0!=45  #35!=45 #50!=45
   guess = int(input("guess number :"))#35 #50 #45
   if(guess==number):#0==45  #35==45 #50==45 #45==45
      print("congratulation ! you won")
      break
   elif(guess<number): #35<45 #50<45
      print("number is greater than" , guess)
   else:
      print("number is smaller than" , guess)

#print 1-5 numbers using while loop
num = 1 #inirilization
while(num<=5): #condition #1<=5 #2<=5 #3<=5  #4<=5 #5<=5 #6<=5
   print(num) #1 2 3 4
   num+=1 #num=num+1 #2 3 4 5 6