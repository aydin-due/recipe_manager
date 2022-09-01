from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        # obj = Article.object.get(id=1)
        # set something
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # obj.save()
        # do something