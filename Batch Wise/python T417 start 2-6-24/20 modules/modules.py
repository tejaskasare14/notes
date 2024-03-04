#module is python file, consist of variables,functions or classes but 
#this python file (module) executes externally
name = "i am module"
def add(a,b):
   result = a+b
   return result

if __name__=="__main__":
   print("file is executed internally")
else:
   print("file is executed externally")

 