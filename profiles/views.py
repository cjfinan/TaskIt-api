from django.shortcuts import render
from rest_framework import generics
from .serializers import ProfileSerializer
from .models import Profile


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
