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

def wholeClass(request):
        posts = Post.objects.filter(category = "class")
        context = {
                "posts":posts,
        }
        return render(request, 'class_k/wholeClass.html',context) 

def wholeFund(request):
        posts = Post.objects.filter(category = "fund")
        context = {
                "posts":posts,
        }
        return render(request, 'funding/wholeFund.html',context)  

def createCla(request):
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
                return redirect(wholeClass)

def createLec(request):
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

def createFund(request):
        if request.method == "GET":
                return render(request, 'funding/createFund.html')

        elif request.method == "POST":
                post = Post()
                post.user = request.user
                post.title = request.POST['title']
                post.region = request.POST['region']
                post.subject = request.POST['subject']
                post.content = request.POST['content']
                post.max_money = request.POST['max_money']
                post.category = "fund"
                post.pic = request.FILES.get('pic','default')
                post.save()
                return redirect(wholeFund)

def read(request,post_id):
        post = Post.objects.get(id = post_id)
        comment = Comment.objects.filter(post=post.id)
        context={
                "post":post,
                "comment":comment,
        }
        return render(request, 'read.html',context)


def fund(request,post_id):
        post = Post.objects.get(id = post_id)
        comment = Comment.objects.filter(post=post.id)
        context={
                "post":post,
                "comment":comment,
        }
        return render(request, 'funding/fund.html',context)

def money(request,post_id):
        post = Post.objects.get(id = post_id)
        money = int(request.GET['money'])
        post.now_money += money
        post.save()
        return redirect('fund', post_id)

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
        return redirect(index)


def c_create(request,post_id):
        if request.method == "POST":
                comment = Comment()
                comment.user = request.user
                comment.post = Post.objects.get(id=post_id)
                comment.content = request.POST['comment']
                comment.save()
                return redirect(read,comment.post.id)