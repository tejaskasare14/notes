from django.shortcuts import render
from django.http import HttpResponse
from user_generalform.models import User

# Create your views here.
def show_user(request):
   return HttpResponse("User added to the table")

def add_user(request):
   if request.method == 'POST':
      user_name=request.POST['name']
      user_designation=request.POST['designation'] 
      user=User.objects.create(name=user_name,designation=user_designation)
      user.save()
      return show_user(request)
   return render(request,'user_generalform/add_user.html')




   