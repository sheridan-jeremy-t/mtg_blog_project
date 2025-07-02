"""Models for MTG Site"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Topic(models.Model):
    """Creating the Topic models"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Post(models.Model):
    """Creating the models for Post"""
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mtg_posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published = models.DateTimeField(null=True,blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    topics = models.ManyToManyField(Topic, blank=True, related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        #Set timestamp when published
        if self.status == 'published' and not self.published:
            self.published = timezone.now()
        elif self.status =='draft':
            self.published = None

        super().save(*args,**kwargs)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
