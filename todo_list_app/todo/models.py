from django.db import models
from django.utils import timezone


class TodoItem(models.Model):
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
