from django.conf import settings
from django.db import models
from .validators import validate_unit

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=228)
    description = models.TextField(blank=True, null=True)
    directions = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=228)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=50, validators=[validate_unit])
    directions = models.CharField(max_length=228, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

# class RecipeImage(models.Model):
#     recipe = models.ForeignKey(Recipe)
