import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    # tags = models.ManyToManyField(Tag)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_published <= now

    def __str__(self):
        return self.title
