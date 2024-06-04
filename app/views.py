from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Task
from . serializers import TaskSerializers, RegisterSerializer
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listTask(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(owner=request.user)
        serializer = TaskSerializers(tasks, many=True)
        if not tasks.exists():
            return Response({'message': 'You currently have no tasks.'}, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data)
    else:
        return Response({'error': 'You are not authenticated.'}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_detail(request, task_name):
    task = Task.objects.get(name=task_name)

    if task.owner != request.user:
        return Response({'detail': 'Voce nao tem acesso a essa tarefa'}, status=status.HTTP_403_FORBIDDEN)


    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, task_name):
    task = Task.objects.get(name=task_name)
    if task.owner != request.user:
        return Response('You dont have permission to delete this task',status=status.HTTP_403_FORBIDDEN)
    task.delete()
    return Response({'message': 'Task deleted.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def list_update(request, task_name):
    task = Task.objects.get(name=task_name)
    if task.owner != request.user:
        return Response('You dont have permission to update this task',status=status.HTTP_403_FORBIDDEN)
    serializer = TaskSerializers(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
    return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
