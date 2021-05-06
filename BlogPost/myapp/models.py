from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

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

    def get_absolute_url(self, ):
        return reverse('myapp:detailview', args=[self.pk])

class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment from {self.name} - {self.body}"