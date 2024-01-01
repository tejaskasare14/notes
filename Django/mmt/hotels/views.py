from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hotels(request):
   msg = "<h1> welocome to MMT hotels </h1>"
   # return HttpResponse(msg)
   return render(request,'hotels/index.html')
