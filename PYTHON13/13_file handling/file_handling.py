# the following options are avaiable to open file in python
# in python we can perform opetaion on text(t) or binary(b) files
# w,r,a,wt,rt,at,wb,rb,ab

import os
file_exist=os.path.isfile("C:/TEJAS KASARE (Very imp folder)/my notes/PYTHON13/13_file handling/demo.txt")

if(file_exist):
   #print("this file exist")
   #READING DATA FROM FILE
   #my_file=open('demo.txt','r')
   # data = my_file.read() #read all file data at a time
   # data = my_file.read(5) #read first 5 character from file
   # data = my_file.readline() #read one line at a time
   #data = my_file.readlines() #read all line from file and return into a list
   #print(data) 
   
   #WRITE DATA INTO FILE
   #we can only write string data into file
   
   #my_file=open('demo.txt','w') #w mode eliminate existing data and add new one
   my_file=open('demo.txt','a') #a mode keep existing data and add new one
   #my_file.write("This is new dynamic line from code \n")
   
   #my_file.write(10) #ERROR
   my_file.write("10") #this is the way to write numbers into file
   
   print("data appended to the file")
   my_file.close()
else:
   print("file not available")