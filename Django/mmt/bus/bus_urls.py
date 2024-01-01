from django.urls import path
from bus import views

urlpatterns = [
    path('home/', views.bus),
]
