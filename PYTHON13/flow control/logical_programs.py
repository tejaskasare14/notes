for r in range(1,4,1):
   for c in range(1,4,1):
      print(1, end="     ")
   print() 
   
print("-----------------------------")


for r in range(1,4,1):
   for c in range(1,4,1):
      if(c<=r):
         print(c,end=" ")
   print()
   
print("-----------------------------")

for r in range(1,4,1):
   for c in range (3,0,-1):
      if(c<=r):
         print(c, end="")
      else:
         print(" ", end="")
   print()
   
   
print("-----------------------------")
for r in range(3,0,-1):
   for c in range (1,4,1):
      if (c<=r):
         print(c,end="")
      else:
         print(" ",end="")
   print()








