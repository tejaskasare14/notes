from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_flight(request):
   msg = "<h1>Welcome to MMT-FLIGHT SERVICE</h1>"
   return HttpResponse(msg)
