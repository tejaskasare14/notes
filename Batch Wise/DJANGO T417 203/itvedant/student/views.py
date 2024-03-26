from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_student(request):
   # msg = "Hello Student"
   # return HttpResponse(msg)
   return render(request,"student/home.html")

   
