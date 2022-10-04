from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.utils.timezone import timezone
from tinymce import models as tinymce_models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')
        
    def save(self, *args, **kwargs):
        super().save()
        
    def __str__(self):
        return self.title
    

class TutorialPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home')
        
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='https://res.cloudinary.com/volendam/image/upload/v1663526963/tsgvlrz1ews9u371xyfj.jpg')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} profile'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.user.username} Comment'