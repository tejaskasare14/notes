from django.urls import path
from newsapp import views

urlpatterns = [
    path('home/', views.show_base),
    path('sports/', views.sports_news),
]