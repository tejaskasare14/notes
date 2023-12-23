from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hotels(request):
   msg = "<h1> welocome to MMT hotels </h1>"
   return HttpResponse(msg)

def display1(request):
   msg = "<h1> welocome to MMT display1 </h1>"
   return HttpResponse(msg)

def display2(request):
   msg = "<h1> welocome to MMT display2 </h1>"
   return HttpResponse(msg)

def display3(request):
   msg = "<h1> welocome to MMT display3 </h1>"
   return HttpResponse(msg)
