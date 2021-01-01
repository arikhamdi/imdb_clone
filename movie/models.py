from django.db import models

from imdb.settings import LANGUAGE_CODE

CATEGORY_CHOICES = (
    ('action', 'ACTION'),
    ('drama', 'DRAMA'),
    ('comedy', 'COMEDY'),
    ('romance', 'ROMANCE'),
)

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('german', 'GERMAN'),
    ('french', 'FRENCH'),
)

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)
    cast = models.ManyToManyField(Actor)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    release_date = models.DateField()
    views_count = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    trailer = models.URLField(max_length=500, null=True, default='')

    def __str__(self):
        return self.title
