from django.urls import path
from bus import views
urlpatterns = [
    path('show/', views.show_bus),
    path('update/', views.update_bus),
    path('delete/', views.delete_bus),
]
