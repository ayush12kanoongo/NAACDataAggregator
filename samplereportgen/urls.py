from student import request_views
from samplereportgen import views
from django.urls import path
urlpatterns = [
    path('', views.displayhomepage),
    path('downloadreport/', request_views.table5p2p2),
]