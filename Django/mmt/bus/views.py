from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bus(request):
   msg = "<h1> welocome to MMT bus </h1>"
   return HttpResponse(msg)
