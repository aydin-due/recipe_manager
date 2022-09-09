from multiprocessing.dummy import Manager
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.urls import reverse
from .utils import slugify_instance_title

# Create your models here.
class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)

class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)


    def search(self, query=None):
        print(query)
        # if query is None or query == "":
        #     return self.get_queryset().none()
        # lookups = Q(title__icontains=query) | Q(content__icontains=query)
        # return self.get_queryset().filter(lookups)
        return self.get_queryset().search(query=query)

class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True, unique=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    publish = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    objects = ArticleManager()

    def get_absolute_url(self):
        # return f'/articles/{self.slug}'
        return reverse('article-detail', kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # obj = Article.object.get(id=1)
        # set something
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        # if self.slug is None:
        #     slugify_instance_title(self, save=False)
        super().save(*args, **kwargs)
        # obj.save()
        # do something

def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        instance = slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance = slugify_instance_title(instance, save=True)
        
post_save.connect(article_post_save, sender=Article)
