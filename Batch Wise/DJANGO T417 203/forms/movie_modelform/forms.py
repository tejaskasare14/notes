from django import forms
from movie_modelform.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
       model=Movie
      #  exclude=['name']
      #  fields = ('genere',)
       fields = '__all__'
