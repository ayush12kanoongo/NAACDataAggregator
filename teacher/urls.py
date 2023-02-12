from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from teacher import request_views
urlpatterns = [
    path('home/',request_views.displayhome),
    path('criteria_page/', request_views.display_criteria_page)
    ]