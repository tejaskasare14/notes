data = [22,33,44,55,11,66]
even_nums=[]
for num in data:
   if(num%2==0):
      even_nums.append(num+5)     
print(even_nums)

even_list = [i+5 for i in data if(i%2==0)]
print(even_list)
