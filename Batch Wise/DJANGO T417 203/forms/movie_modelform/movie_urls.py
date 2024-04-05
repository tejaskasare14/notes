from django.urls import path,include
from movie_modelform import views

urlpatterns = [
    path('add/', views.add_movie)
]
