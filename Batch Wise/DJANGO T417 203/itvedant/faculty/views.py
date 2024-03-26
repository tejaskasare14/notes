from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_faculty(request):
   msg = "Hello Faculty"
   return HttpResponse(msg)