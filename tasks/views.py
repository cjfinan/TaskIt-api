from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework import generics
from .models import Task
from taskit_api.permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializer
from django.db.models import Count, Q
from django.http import JsonResponse
from rest_framework.views import APIView


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('end_date')
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        'owner__profile',
        'status',
        'board',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
