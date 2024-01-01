from django.urls import path
from hotels import views

urlpatterns = [
    path('home/', views.hotels),
]
