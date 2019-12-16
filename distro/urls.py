from django.urls import path
from distro.views import *
app_name = 'distro'

urlpatterns = [
    path('entry',entry,name="entry"),
    path('viewv',viewv,name="viewv"),
    path('personal',personal,name="personal"),
]