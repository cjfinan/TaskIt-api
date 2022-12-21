from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import ProfileSerializer
from .models import Profile
from taskit_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        tasks_count=Count('owner__task', distinct=True),
        boards_count=Count('owner__board', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'tasks_count',
        'boards_count',
        'todo_count',
    ]
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.annotate(
        tasks_count=Count('owner__task', distinct=True),
        boards_count=Count('owner__board', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
