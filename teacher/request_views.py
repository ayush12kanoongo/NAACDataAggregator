from django.shortcuts import render
from teacher import db_connect_views
# Create your views here.
def table2p4p1and2p4p3(request):
    # Authenticaion of request
    return db_connect_views.table2p4p1and2p4p3(request)

def table3p1p2and3p1p2p1(request):
    # Authenticaion of request
    return db_connect_views.table3p1p2and3p1p2p1(request)

def table3p1p3(request):
    # Authenticaion of request
    return db_connect_views.table3p1p3(request)

def table3p4p3(request):
    # Authenticaion of request
    return db_connect_views.table3p4p3(request)


def table3p5p1(request):
    # Authenticaion of request
    return db_connect_views.table3p5p1(request)

def table3p5p2(request):
    # Authenticaion of request
    return db_connect_views.table3p5p2(request)

def table6p3p2(request):
    # Authenticaion of request
    return db_connect_views.table6p3p2(request)

def table6p3p4(request):
    # Authenticaion of request
    return db_connect_views.table6p3p4(request)

def displayhome(request):
    # Authentication of request
    return db_connect_views.displayhome(request)

def display_criteria_page(request):
    #Authentication of request
    return db_connect_views.display_criteria_page(request)