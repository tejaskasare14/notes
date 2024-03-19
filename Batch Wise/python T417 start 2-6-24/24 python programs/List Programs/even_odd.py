#find even and odd numbers from given list
#on dividing any number by two, if we get reminder zero, then it is even number
data = [25,46,8,76,9,69,7]
even_list = []
odd_list = []
for num in data:
   if(num%2==0):
      even_list.append(num)
   else:
      odd_list.append(num)

print("there are total {} even numbers in given list".format(len(even_list)))
print("those are {}".format(even_list))

print("there are total {} odd numbers in given list".format(len(odd_list)))
print("those are {}".format(odd_list))
      

