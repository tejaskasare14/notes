#opening file which is not exist
#open("testy.txt","r")  #FileNotFoundError: [Errno 2] No such file or directory: 'testy.txt'
#print("File exist")

#how to check perticular file exist
#import os
#is_file_exist1 = os.path.isfile("test.txt")
#print(is_file_exist1)

#is_file_exist2 = os.path.isfile("C:/TEJAS KASARE (Very imp folder)/my notes/Batch Wise/MERN start - 24-2-24/JS/index.html")
#print(is_file_exist2)

#reading data from file
import os
file_name = "test.txt"
is_file_exist = os.path.isfile(file_name)

if(is_file_exist):
   my_file = open("test.txt","r")
   #print(my_file.read()) #read() all data from file
   #print(my_file.read(5)) #read(5) first five characters from file
   #print(my_file.readline()) #one line at a time
   #print(my_file.readline()) #one line at a time (next line)
   print(my_file.readlines())
   my_file.close()
   
else:
   print("No file with found with name : ",file_name)
