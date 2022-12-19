from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = (
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    HIGH = 3
    NORMAL = 2
    LOW = 1
    PRIORITY_CHOICES = (
        (HIGH, 'High'),
        (NORMAL, 'Normal'),
        (LOW, 'Low'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='to_do')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=NORMAL)
    
    class Meta:
        ordering = ['-created_at']
