from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['ID'], password=request.POST['password1'])
            user.profile.name= request.POST['name']
            user.profile.region = request.POST['region']
            user.profile.sex = request.POST['sex']
            user.profile.phone = request.POST['phone']
            user.profile.job = request.POST['job']
            user.profile.field = request.POST['field']
            user.profile.age = request.POST['age']

            auth.login(request, user)
            return redirect('index')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['ID']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'ID or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return render(request, 'signup.html')