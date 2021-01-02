from django.db import models
from autoslug import AutoSlugField

from imdb.settings import LANGUAGE_CODE


LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('japanese', 'JAPANESE'),
    ('french', 'FRENCH'),
)

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


class Actor(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name',
                         max_length=100,
                         unique_for_date='created')
    created = models.DateTimeField(auto_now_add=True)
    birth_name = models.CharField(max_length=100)
    born_date = models.DateField()
    born_place = models.CharField(max_length=100)
    height = models.IntegerField(default=0)
    bio = models.TextField()
    image = models.ImageField(upload_to='actors')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name',
                         max_length=50,
                         unique_for_date='created')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title',
                         max_length=250,
                         unique_for_date='created')
    description = models.TextField()
    image = models.ImageField(upload_to='movies')
    category = models.ManyToManyField(Category)
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


class Banner(models.Model):
    banner = models.ImageField(upload_to='slder')
    created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(
        Movie, related_name='movie_banner', on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title
