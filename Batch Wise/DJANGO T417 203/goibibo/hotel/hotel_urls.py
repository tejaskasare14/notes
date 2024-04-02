from django.urls import path
from hotel import views
urlpatterns = [
    path('show/', views.show_hotel),
    path('update/', views.update_hotel),
    path('delete/', views.delete_hotel),
]
