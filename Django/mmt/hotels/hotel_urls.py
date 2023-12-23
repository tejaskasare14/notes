from django.urls import path
from hotels import views

urlpatterns = [
    path('', views.hotels),
    path('display1/', views.display1),
    path('display2/', views.display2),
    path('display3/', views.display3),
]
