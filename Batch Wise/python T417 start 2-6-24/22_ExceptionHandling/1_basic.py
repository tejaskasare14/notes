
# x = int(input("Enter first number :"))#risky code
# y = int(input("Enter second number :"))#risky code
# result = x/y #risky code
# print(result)
# print("hi")




# result = 0
# try:
#    x = int(input("Enter first number :"))#risky code
#    y = int(input("Enter second number :"))#risky code
#    result = x/y #risky code
# except ZeroDivisionError:
#    print("you can not divide any number by zero") #handling code
# except ValueError:
#    print("Bhai... Number enter kar...")#handling code
# print(result)
# print("hi")

result = 0
try:
   x = int(input("Enter first number :"))#risky code
   y = int(input("Enter second number :"))#risky code
   result = x/y #risky code
except ZeroDivisionError:
   print("you can not divide any number by zero") #handling code
# except ValueError:
#     print("Bhai... Number enter kar...")#handling code
finally:
   print("i will execute even if the exception is not handled")
print(result)
print("hi")




print(10/0)
try:
   print("try")
except:
   print("except")
finally:
   print("finally")


