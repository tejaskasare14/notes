from django.shortcuts import render

# Create your views here.
import datetime
def show_base(request):
   employee = {"id":"TCS-1","name":"raj","city":"pune","dob":datetime.datetime.now()}
   return render(request,'base.html',context=employee)

def sports_news(request):
   return render(request,'sports/sports.html')
