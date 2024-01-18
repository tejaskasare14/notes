from django.urls import path
from myapp import views

urlpatterns = [
    path('view/', views.view),
]
