from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)