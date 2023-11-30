#printing 1 -5 numbers using recurssion
def recursive(start,end):
   if(start<=end):
      print(start)
      start+=1
      recursive(start,end)
recursive(1,10)

