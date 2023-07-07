from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Comment(models.Model):  
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=50,null=True)
    body = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    
from django.utils import timezone

class message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    