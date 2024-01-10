from django import forms

class MovieForm(forms.Form):
   name=forms.CharField(max_length=15)
   release_date=forms.DateField()
   INTHEATERS_CHOICES = (
   ('yes', 'Yes'),
   ('no', 'No'))
   in_theater = forms.ChoiceField(choices=INTHEATERS_CHOICES,)
   rating = forms.FloatField()
   LANGUAGE_CHOICES = (
   ('hindi', 'Hindi'),
   ('marathi', 'Marathi'),
   ('english', 'English'))
   language = forms.ChoiceField(choices=LANGUAGE_CHOICES)
   
   
  