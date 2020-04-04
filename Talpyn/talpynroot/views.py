from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'talpynroot/index.html')

def temp(request):
    return render(request, 'talpynroot/temp.html')