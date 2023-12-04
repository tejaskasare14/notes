s = "a2b3c1"
final_string=""
for i in range(0,len(s)):
   if(s[i].isalpha()):
      continue
   else:
      for j in range(0,int(s[i])):
         final_string+=s[i-1]
         
print(final_string)