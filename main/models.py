from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    region = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)
    option = models.CharField(max_length = 100)
    like = models.ManyToManyField(User, related_name='likes',blank=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    pic = models.ImageField(upload_to='images/',null=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    post = models.ForeignKey(Post,on_delete=models.CASCADE) 
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50) 
	region = models.CharField(max_length=50)
    age = models.DateField(blank=True)
    field = models.TextField(blank=True)
    job = models.CharField(max_length=50)