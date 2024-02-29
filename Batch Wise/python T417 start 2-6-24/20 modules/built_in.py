#datetime,calendar
#datetime module
import datetime

todays_date= datetime.date.today()
print(todays_date)
todays_date_withtime= datetime.datetime.now()
print(todays_date_withtime)


my_date = datetime.datetime.now()
print(my_date)
print(my_date.strftime("%d")) #day of the month
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

