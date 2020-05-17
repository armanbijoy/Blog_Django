from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    

class Blog(models.Model):
    title = models.CharField(max_length=255, null = True)
    body = models.TextField(null = True)
    author = models.ForeignKey(User, models.CASCADE)
    category = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_post')
    
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        
        return str(self.author)+'|'+ self.title
    def get_absolute_url(self):
        return reverse('home')
    
   