from django.shortcuts import render
from movie.models import MovieTable
from movie import forms 

# Create your views here.
def view_movies(request):
   result = MovieTable.objects.all()
   print(result)
   data = {'movie_list':result}
   return render(request,'movie/view_movies.html',context=data)

def add_movies(request):
   form = forms.MovieForm()
   if request.method == "POST":
      form=forms.MovieForm(request.POST)
      if (form.is_valid()):
         obj = MovieTable()
         obj.name = form.cleaned_data['name']
         obj.release_date = form.cleaned_data['release_date']
         obj.in_theater = form.cleaned_data['in_theater']
         obj.rating = form.cleaned_data['rating']
         obj.language = form.cleaned_data['language']
         obj.save()
         return view_movies(request)   
   data = {'movie_form':form}
   return render(request,'movie/add_movies.html',context=data)


