from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(auto_now_add=False, blank=True)
    end_date = models.DateTimeField(auto_now_add=False, blank=True)

    class Meta:
        ordering = ['-created_at']
