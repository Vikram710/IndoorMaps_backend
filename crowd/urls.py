from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('distro/api/',include('distro.urls')),
    path('parking/api/',include('parking.urls')),
    
]
