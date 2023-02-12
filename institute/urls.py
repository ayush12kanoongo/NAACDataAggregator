from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from institute import request_views
urlpatterns = [
    path('home/', request_views.displayhome),
]
