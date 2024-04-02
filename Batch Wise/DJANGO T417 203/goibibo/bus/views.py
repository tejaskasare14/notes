from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_bus(request):
   return HttpResponse("Showing Bus")

def update_bus(request):
   return HttpResponse("Updating Bus")

def delete_bus(request):
   return HttpResponse("Deleting Bus")
