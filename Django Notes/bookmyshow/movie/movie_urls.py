from django.urls import path
from movie import views

urlpatterns = [
    path('home/', views.show_movies),
]