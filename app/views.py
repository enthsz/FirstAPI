from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Task
from . serializers import TaskSerializers
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listTask(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(owner=request.user)
    else:
        return Response('adwwd ')
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_detail(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
    return Response(serializer.data)

@api_view(['DELETE', 'GET'])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    if task.owner != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def list_update(request, pk):
    task = Task.objects.get(pk=pk)
    if task.owner != request.user:
        return Response(status=status.HTTP_403_FORBIDDEN)
    serializer = TaskSerializers(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
    return Response(serializer.data)

