from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField(blank = True)
    region = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)
    like = models.ManyToManyField(User, related_name='likes',blank=True)
    pic = models.ImageField(upload_to='images/',null=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)

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
    sex = models.TextField(blank = True)
    age = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    job = models.TextField(blank = True)
    field = models.TextField(blank = True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()