from django.shortcuts import render
from rest_framework import generics
from .models import Task
from taskit_api.permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializer


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
