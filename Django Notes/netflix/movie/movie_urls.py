from django.urls import path
from movie import views

urlpatterns = [
    path('view/', views.view_movies),
    path('add/', views.add_movies),
]