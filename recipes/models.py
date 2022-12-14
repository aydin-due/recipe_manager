from django.conf import settings
from django.db import models
from .validators import validate_unit
from .utils import number_str_to_float

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
    quantity_as_float = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit])
    directions = models.CharField(max_length=228, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        quantity = self.quantity
        quantity_as_float, success = number_str_to_float(quantity)
        if success:
            self.quantity_as_float = quantity_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)

# class RecipeImage(models.Model):
#     recipe = models.ForeignKey(Recipe)
