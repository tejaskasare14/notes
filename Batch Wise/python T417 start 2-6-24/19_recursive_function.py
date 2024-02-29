
#recusrive function :  when function calls itself
def add():
   sum = 12+2
   print(sum)
   add()
#add()
#7 ->3,4,5,6,3,4,5,6,3
#RecursionError: maximum recursion depth exceeded

#print 1-10 numbers without using any loop
def range_1_10(start,end):#start:1,end:10  | start:2,end:10
   if(start<=end):#1<=10 | 2<=10
      print(start)#1 | 2
      start+=1#start = 2 | start=3
      range_1_10(start,end)#range_1_10(2,10) | range_1_10(3,10)

range_1_10(1,10)
   
   
#print sum of 1-5 numbers without using any loop
sum=0
def sum_1_5(start,end):
   if(start<=end):
      global sum
      sum+=start
      start+=1
      sum_1_5(start,end)
sum_1_5(1,5)
print(sum)