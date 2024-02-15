from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request,'pages/index.html')

def About  (request):
    return render (request,'pages/about.html')