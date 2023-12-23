from django.urls import path
from bus import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hotels/', hotel_views.hotels),
     path('bus/', bus_views.bus),
]
