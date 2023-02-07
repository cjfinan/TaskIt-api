from django.db.models import Count
from django.shortcuts import render
from rest_framework import generics
from .serializers import BoardSerializer
from .models import Board
from taskit_api.permissions import IsOwnerOrReadOnly


class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all().order_by('-created_at')
    serializer_class = BoardSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.annotate(
        boards_count=Count(
            'owner__board', distinct=True
        )
    ).order_by('-created_at')
    serializer_class = BoardSerializer
    permission_classes = [IsOwnerOrReadOnly]
