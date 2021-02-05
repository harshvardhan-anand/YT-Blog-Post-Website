from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Post(models.Model):

    choice = (
        ('published', 'PUBLISHED'),
        ('draft', 'DRAFT')
    )

    title = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(choices = choice, max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    new_manager = PublishedManager()

    def __str__(self):
        return self.title