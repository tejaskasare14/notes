import os
file_name = "alice_in_wonderland.txt" 
is_file_exist = os.path.isfile(file_name)

if(is_file_exist):
   my_file=open(file_name,"r")
   #reading all from file
   data = my_file.read()
   # print(data)
   #getting total words present in data
   all_words = data.split(" ")
   #print(all_words)
   filterd_Words = []
   for word in all_words:
      if(word.isalpha()):
         filterd_Words.append(word)
      # else:
      #    a = []
      #    b=word.split("\n")
      #    for w in b:
      #       if(w.isalpha):
      #          filterd_Words.append(w)
   print(filterd_Words)
      
   count = len(filterd_Words)
   print(count)
   my_file.close()
   # my_file2=open("word_count.txt","a")
   # my_file2.write("There are "+str(count)+" words present in given file\n")
   # print("word count added")
   # my_file2.close()
else:
   print("File not exist")
