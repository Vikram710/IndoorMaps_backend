from django.urls import path
from distro.views import *
app_name = 'distro'

urlpatterns = [
    path('entry',entry,name="entry"),
    path('rpfreq',viewv,name="viewv"),
    path('personal',personal,name="personal"),
    path('get_coord',get_coord),
    path('draw_path',draw_path),
    path('locate_me',locate_me),
]