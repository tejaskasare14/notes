from django.shortcuts import render
from movie_modelform.forms import MovieForm
from django.http import HttpResponse

# Create your views here.

def show_movie(request):
   return HttpResponse("Movie added to the table")

def add_movie(request):
   if request.method=='POST':
      movie_form = MovieForm(request.POST)
      if(movie_form.is_valid()):
         movie_form.save()
      return show_movie(request)
   data={}
   form=MovieForm()
   data['movie_form']=form
   return render(request,'movie_modelform/add_movie.html',context=data)


