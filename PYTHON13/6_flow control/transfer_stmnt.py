prices = [199,299,99,199,399]

#break -> terminate the loop based on condition
#continue -> skip current iteration and go for next based on condition
#pass -> use this pass keyword when you dont want to write any code for a block/suit/body

for price in prices:
   if(price==99):
      print("terminating the loop because i got 99")
      break
      print("i am after break") #this LOC will not execute
   else:
      print(price, "added to cart")
 
print("----  continue  ------") 
      
for price in prices:
   if(price==99):
      #print("skipping the current iteration because i got 99")
      continue
      print("i am after continue") #this LOC will not execute
   else:
      print(price, "added to cart")
      
if(10>5):
   pass #use this pass keyword when you dont want to write any code for a block/suit/body
   
   
   
   