#there are 3 transfer statements in python : pass,break,continue
#pass : to show empty block of code
#break : to terminate the loop based on condition
#continue : skip current iteration and go for next based on condition

#any code you write after pass,break or continue will not execute

#pass
marks = [99,35,45,95]
for mark in marks:
   if(mark<80):
      pass
   else:
      print(mark)

#break
prices = [99,199,299,99,399,199]
for price in prices:
   if(price==199):
      print("I am breaking the loop")
      break #from here it will go to line 22
      print("hiiii")
   else:
      print(price, " added to cart")
print("I am out of loop")

#conitnue
prices = [99,199,299,99,399,199]
for price in prices:
   if(price==199):
      print("I going for next interation")
      continue  #from here it will go to line 26      
   else:
      print(price, " added to cart")

print("I am out of loop")
