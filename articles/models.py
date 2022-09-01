from django.db import models
from django.db.models.signals import pre_save, post_save
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
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        # obj.save()
        # do something

def article_pre_save(sender, instance, *args, **kwargs):
    print('presave')
    print(sender, instance)
    if instance.slug is None:
        instance.slug = slugify(instance.title)

def article_post_save(sender, instance, created, *args, **kwargs):
    print('postsave')
    print(args, kwargs)
    if created:
        instance.slug = 'this is my slug'
        instance.save()


pre_save.connect(article_pre_save, sender=Article)
post_save.connect(article_post_save, sender=Article)
