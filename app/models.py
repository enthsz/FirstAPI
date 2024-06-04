from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    data_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username