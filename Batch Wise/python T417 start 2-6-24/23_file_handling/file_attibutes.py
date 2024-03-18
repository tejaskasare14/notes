my_file=open("test.txt","r")

print(my_file.name)
print(my_file.mode)
print(my_file.closed)

my_file.close()
print(my_file.closed)

#opening file with "with"
print('opening file with "with"')
with open("test.txt","r") as test_file:
   print(test_file.name)
   print(test_file.closed)



print(test_file.closed)