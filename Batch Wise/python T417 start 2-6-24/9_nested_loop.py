#print below pattern
#1 2 3
#1 2 3
#1 2 3

for r in range(1,4):
   for c in range(1,4):
      print(c,end=" ")
   print()
   
#print following pattern
# 2 4 6
# 2 4 6
# 2 4 6
for r in range(1,4):
   for c in range(2,7,2):
      print(c,end=" ")
   print()   

#print follwoing pattern
# AB BB CB
# AB BB CB
# AB BB CB
for r in range(1,4):
   letters = ["AB", "BB", "CB"]
   for letter in letters:
      print(letter, end=" ")
   print()

#print follwoing pattern
# 11 22 33
# 11 22 33
# 11 22 33
for r  in range(1,4):
   for c in range(1,4):
      print(11*c, end=" ")
   print()

#print follwoing pattern
# 9 16 25
# 9 16 25
# 9 16 25
for r in range(1,4):
   for c in range(3,6):
      print(c**2,end=" ")
   print()
#print follwoing pattern
# 1 4 27 
# 1 4 27
# 1 4 27
for r in range(1,4):
   for c in range(1,4):
      print(c**c,end=" ")
   print()
   
#print follwoing pattern
# 1
# 1 2
# 1 2 3
for r in range(1,4):
   for c in range(1,4):
      if(c<=r):
         print(c,end=" ")
   print()
   
#print follwoing pattern
#     1
#   2 1
# 3 2 1
print(list(range(3,0,-1))) #[3,2,1]
for r in range(1,4):
   for c in range(3,0,-1):
      if(c<=r):
         print(c,end="")
      else:
         print(" ",end="")
   print()
   
#print follwoing pattern
#3 2 1
#  2 1
#    1
   


