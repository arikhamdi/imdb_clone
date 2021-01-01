from django.contrib.admin.filters import FieldListFilter
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Movie


class MovieList(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'


class MostWatched(ListView):
    model = Movie
    paginate_by = 1
    template_name = 'movie/most_watched.html'

class RecentlyAdded(ListView):
    model = Movie
    paginate_by = 1
    template_name = 'movie/recently_added.html'

class TopRated(ListView):
    model = Movie
    paginate_by = 1
    template_name = 'movie/top_rated.html'

    
