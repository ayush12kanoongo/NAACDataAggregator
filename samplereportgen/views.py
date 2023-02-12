from django.shortcuts import render

# Create your views here.
def displayhomepage(request):
    rend= render(request,'samplereportgen/home.html')
    return rend
