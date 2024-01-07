#print 1-5 numbers
for x in range(1,6,1):
   print(x)
   
#print even numbers between 1-10(include)
for x in range(1,11,1):
   if(x%2==0):
      print(x , " is even number")
      
#print 5-1 numbers
for x in range(5,0,-1):
   print(x)
   
# print 1-5 using while loop
print("print 1-5 using while loop")
a = 1
while(a<=5):
   print(a)
   a+=1
   
   
#print characters in given string
s="hello"
for char in s:
   print(char,end=",")
   
   
print()
   
#print items in given list
marks = [98,96,95,99]
for mark in marks:
   print(mark,end=",")
   
#print even numbers those are greater than 20 in given list
data = [2,6,3,44,98,22,35] #44,98,22
   

