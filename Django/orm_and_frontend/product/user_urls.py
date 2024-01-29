from django.urls import path
from product import views

urlpatterns = [
    path('register/', views.register_user),
    path('login/', views.login_user),
    path('logout/', views.user_logout),
]
