from django.shortcuts import render

# Create your views here.
def show_base(request):
   return render(request,'base.html')

def sports_news(request):
   return render(request,'sports/sports.html')
