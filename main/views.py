from django.shortcuts import render, redirect;

def index(request):

    return render(request,'index.html')

# Create your views here.

def intro(request):
    return render(request, 'kangmin/intro.html')
def notion(request):
    return render(request, 'kangmin/notion.html')
def QnA(request):
    return render(request, 'kangmin/QnA.html')


def wholeLecture(request):
        return render(request, 'lecture/wholeLecture.html')
def localLecture(request):
    return render(request, 'lecture/localLecture.html')
def subjectLecture(request):
    return render(request, 'lecture/subjectLecture.html')


def wholeClass(request):
    return render(request, 'class_k/wholeClass.html')
def localClass(request):
    return render(request, 'class_k/localClass.html')
def subjectClass(request):
    return render(request, 'class_k/subjectClass.html')


def lectureFunding(request):
    return render(request, 'funding/lectureFunding.html')
def classFunding(request):
    return render(request, 'funding/classFunding.html')
def fundingResult(request):
    return render(request, 'funding/fundingResult.html')


def createLec(request):
    if request.method == "GET":
        return render(request, 'lecture/createLec.html')
def createCla(request):
    if request.method == "GET":
        return render(request, 'class_k/createCla.html')