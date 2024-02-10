import os
file_exist=os.path.isfile("C:/TEJAS KASARE (Very imp folder)/my notes/PYTHON13/13_file handling/story.txt")

if(file_exist):
   count = 0
   my_file=open("alice_in_wonderland.txt","r")
   for line in my_file:
      print(line)
      words=line.split(" ")
      print(words, len(words))
      count=count+len(words)
   print("total words are : ", count)
   my_file.close()
   word_count_file=open("word_count.txt","w")
   word_count_file.write("there are "+str(count)+" words in given file")
   word_count_file.close()
else:
   print("file not available")