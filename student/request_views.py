from django.shortcuts import render
from student import db_connect_views
# Create your views here.

def table1p3p4and1p3p4p1(request):
    # Authenticaion of request
    return db_connect_views. table1p3p4and1p3p4p1(request)

def table2p7p1(request):
    # Request Authentication and checks here
    return db_connect_views.table2p7p1(request)

def table5p1p1and5p1p2(request):
    # Authenticaion of request
    return db_connect_views. table5p1p1and5p1p2(request)

def table5p2p1(request):
    # Authenticaion of request
    return db_connect_views.table5p2p1(request)

def table5p2p2(request):
    # Authenticaion of request
    return db_connect_views. table5p2p2(request)

def table5p2p3(request):
    # Authenticaion of request
    return db_connect_views. table5p2p3(request)

def table5p3p1(request):
    # Authenticaion of request
    return db_connect_views. table5p3p1(request)

def displayhome(request):
    # Authentication of request
    return db_connect_views.displayhome(request)

def displayacademicinfo(request):
    #Authentication of request
    return db_connect_views.displayacademicinfo(request)
