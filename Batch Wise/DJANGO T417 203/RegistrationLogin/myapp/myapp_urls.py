from django.urls import path
from myapp import views
urlpatterns = [
    path('register/', views.register_user),
    path('login/', views.login_user),
    path('home/', views.home),
    path('logout/', views.user_logout),
]
