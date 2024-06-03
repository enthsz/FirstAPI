from rest_framework import serializers
from . models import Task
from django.contrib.auth.models import User

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'content', 'owner']



