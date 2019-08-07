from django.shortcuts import render

def index(request):

    return render(request,'index.html')

# Create your views here.

def intro(request):
    return render(request, 'kangmin/intro.html')