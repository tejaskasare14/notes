name = "raj"

def add(x,y):
   return x+y

def sub(x,y):
   return x-y


print(__name__)
if (__name__ == "__main__"):
   print("this file is executed directly")
else:
   print("this file executed by some other file as a modlue")