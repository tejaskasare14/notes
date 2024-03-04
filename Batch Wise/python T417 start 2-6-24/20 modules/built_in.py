#datetime,calendar
#datetime module
import datetime

todays_date= datetime.date.today() #only current date
print(todays_date)
todays_date_withtime= datetime.datetime.now()  # current date with timestamp
print(todays_date_withtime) 


my_date = datetime.datetime.now()
print(my_date)
print(my_date.strftime("%d")) #day of the month (like 4th day of the month)
print(my_date.strftime("%w")) #number of weekday (monday 1....)
print(my_date.strftime("%a")) #weekday name (first 3 character)
print(my_date.strftime("%A")) #weekday name
print(my_date.strftime("%W")) #week of the year
print(my_date.strftime("%b")) #3 charatrs of month name
print(my_date.strftime("%B")) #wcomplete month name
print(my_date.strftime("%m")) #month in decimal
print(my_date.strftime("%y")) #year with2 digits
print(my_date.strftime("%Y")) #year with 4 digits

print(my_date.strftime("%d/%b/%Y")) #29/Feb/2024

#getting dtails from random date
#datetime.datetime(year,month,day,hr,min,sec,microsec)
random_date = datetime.datetime(2024,3,4,11,23,40,452610)
print(random_date)
print(random_date.year)
print(random_date.month)
print(random_date.day)
print(random_date.strftime("%A"))
print("Date is :",random_date.strftime("%d-%b-%Y"))

print(datetime.datetime(2024,3,4,11,23,40,452610))
print(datetime.datetime(2024,3,4))
print(datetime.date(2024,3,4))

#diff between 2 dates
d1 = datetime.date(2024,3,4)
d2 = datetime.date(2024,3,20)
print(d2-d1)
print(d1-d2)

#different ways of importing module

# from math import sqrt
# print(sqrt(49))

# from math import *
# print(sqrt(49))

# import math
# print(math.sqrt(49))

# import math as mathematics
# #print(math.sqrt(49)) #ERROR
# print(mathematics.sqrt(49))

# from math import sqrt as square_root
# # print(sqrt(49)) #ERROR
# print(square_root(49))

# from math import sqrt,ceil
# print(sqrt(49))
# print(ceil(25.05))


# from math import sqrt as square_root,ceil as celing
# print(square_root(49))
# print(celing(25.05))

import math
print(math.sqrt(36))
print(math.ceil(36.06))
print(math.ceil(36.99))
print(math.floor(36.99))
print(math.pow(4,2))
print(math.factorial(3))
print(math.remainder(10,3))








