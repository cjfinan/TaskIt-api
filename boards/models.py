from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    description = description = models.TextField(blank=True)
