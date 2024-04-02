from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_hotel(request):
   return HttpResponse("Showing hotel")

def update_hotel(request):
   return HttpResponse("Updating hotel")

def delete_hotel(request):
   return HttpResponse("Deleting hotel")
