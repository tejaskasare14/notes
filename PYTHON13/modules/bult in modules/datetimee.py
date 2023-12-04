import datetime

today_with_time = datetime.datetime.now()
print(today_with_time)

today_without_time = datetime.date.today()
print(today_without_time)

print(today_with_time.strftime("%a")) #first 3 letters of weekday
print(today_with_time.strftime("%A")) #complete name of weekday
print(today_with_time.strftime("%w")) #number of weekday(monday is 1, tuesday is 2 .....)
print(today_with_time.strftime("%d")) #day of month
print(today_with_time.strftime("%b")) #first 3 letters of month
print(today_with_time.strftime("%B")) #complete name  of month
print(today_with_time.strftime("%y")) #2 digits of year
print(today_with_time.strftime("%Y")) #4 digits of year
print(today_with_time.strftime("%H")) #irst 3 letters of month
print(today_with_time.strftime("%M")) #irst 3 letters of month
print(today_with_time.strftime("%S")) #irst 3 letters of month

#formatting  date
print(today_with_time.strftime("%d/%b/%Y")) #irst 3 letters of month
print("today_with_time is : ",today_with_time.strftime("%A"))

#getting information from random date
random_date = datetime.datetime(2023,12,4,13,45,30,35650)
print(random_date)
print(random_date.strftime("%A"))
print("year", random_date.year)
print("month", random_date.month)
print("day", random_date.day)
print("hour", random_date.hour)
print("min", random_date.minute)
print("sec", random_date.second)
print("micro sec", random_date.microsecond)

x = datetime.date(2023,12,4)
print(x)

#diff between 2 dates
d1 = datetime.date(2023,12,4)
d2 = datetime.date(2023,12,6)
d3 = d2-d1
d4 = d1-d2
print(d3)
print(d4)

d5 = datetime.datetime(2023,12,4,13,45,30,35650)
d6 = datetime.datetime(2023,12,6,14,46,30,35650)
print(d6-d5)






