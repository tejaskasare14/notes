from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
   message = "<h1> welcome to my hotel </h1>"
   return HttpResponse(message)

def test(request):
   message = "<h1> this is test view in hotels app </h1>"
   return HttpResponse(message)
