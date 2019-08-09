from django.shortcuts import render, redirect
from .models import Post,Comment
def index(request):
        return render(request,'index.html')


def intro(request):
        return render(request, 'kangmin/intro.html')
def notion(request):
        return render(request, 'kangmin/notion.html')
def QnA(request):
        return render(request, 'kangmin/QnA.html')


def wholeLecture(request):
        posts = Post.objects.filter(category = "lecture")
        context = {
                "posts":posts,
        }

        return render(request, 'lecture/wholeLecture.html',context)

def localLecture(request):
        posts = Post.objects.filter(category = "lecture")
        context = {
                "posts":posts,
        }

        return render(request, 'lecture/localLecture.html',context)

def subjectLecture(request):
        posts = Post.objects.filter(category = "lecture")
        context = {
                "posts":posts,
        }

        return render(request, 'lecture/subjectLecture.html',context)


def wholeClass(request):
        posts = Post.objects.filter(category = "class")
        context = {
                "posts":posts,
        }

        return render(request, 'class_k/wholeClass.html',context)

def localClass(request):
        posts = Post.objects.filter(category = "class")

        return render(request, 'class_k/localClass.html')

def subjectClass(request):
        posts = Post.objects.filter(category = "class")

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

        elif request.method == "POST":
                post = Post()
                post.user = request.user
                post.title = request.POST['title']
                post.region = request.POST['region']
                post.subject = request.POST['subject']
                post.content = request.POST['content']
                post.category = "lecture"
                post.pic = request.FILES.get('pic','default')
                post.save()     
                return redirect(wholeLecture)

def createCla(request):
        if request.method == "GET":
                return render(request, 'class_k/createCla.html')

        elif request.method == "POST":
                post = Post()
                post.user = request.user
                post.title = request.POST['title']
                post.region = request.POST['region']
                post.subject = request.POST['subject']
                post.content = request.POST['content']
                post.category = "class"
                post.pic = request.FILES.get('pic','default')
                post.save()     
                return redirect(wholeClass)


def read(request,post_id):
        post = Post.objects.get(id = post_id)
        comment = Comment.objects.filter(post=post.id)
        context={
                "post":post,
                "comment":comment,
        }
        return render(request, 'read.html',context)

def update(request,post_id):
        if request.method == "GET":
                post = Post.objects.get(id = post_id)
                context = {
                "post":post,
                }
                return render(request,'update.html',context)

        elif request.method == "POST":
                post = Post.objects.get(id = post_id)
                post.title = request.POST['title']
                post.content = request.POST['content'] 
                post.save()

                return redirect(wholeLecture)

def delete(request,post_id):

        post = Post.objects.get(id = post_id)
        post.delete()
        
        return redirect(wholeLecture)


def c_create(request,post_id):
        if request.method == "POST":
                comment = Comment() 
                comment.user = request.user
                comment.post = Post.objects.get(id=post_id)
                comment.content = request.POST['comment']
                comment.save() 
                return redirect(read,comment.post.id)