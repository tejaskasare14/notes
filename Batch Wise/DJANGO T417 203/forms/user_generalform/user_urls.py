from django.urls import path
from user_generalform import views

urlpatterns = [
    path('add/', views.add_user),
    path('show/', views.show_user),
]