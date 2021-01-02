from django.contrib.admin.filters import FieldListFilter
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie, Actor, Category


class ActorDetail(DetailView):
    model = Actor


class CategoryList(ListView):
    model = Category


class MovieCategory(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'

    def get_queryset(self):
        self.category_name = self.kwargs['name']
        movies = Movie.objects.filter(category__name=self.category_name)
        return movies

    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['list_title'] = self.category_name
        return context


class MovieLanguage(ListView):
    model = Movie
    template_name = 'movie/movie_list.html'

    def get_queryset(self):
        self.language = self.kwargs['lang']
        movies = Movie.objects.filter(language=self.language)
        return movies

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['list_title'] = self.language
        return context


class MovieList(ListView):
    model = Movie
    template_name = 'movie/index.html'

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)
        context['recently_added'] = Movie.objects.all().order_by(
            '-created')[:15]
        context['most_watched'] = Movie.objects.all().order_by(
            '-views_count')[:15]
        context['top_rated'] = Movie.objects.all().order_by(
            '-rating')[:15]
        return context


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.views_count += 1
        object.save()
        return object


class MovieSearch(ListView):
    model = Movie
    paginate_by = 8
    template_name = 'movie/movie_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        self.result = Movie.objects.filter(title__icontains=query)
        return self.result

    def get_context_data(self, **kwargs):
        context = super(MovieSearch, self).get_context_data(**kwargs)
        context['list_title'] = f'Search Result : {self.result.count()}'
        return context


class MovieYearList(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = "release_date"
    make_object_list = True
    allow_future = True
    template_name = 'movie/movie_list.html'


class MostWatched(ListView):
    model = Movie
    paginate_by = 8
    ordering = ['-views_count']
    template_name = 'movie/movie_list.html'

    def get_context_data(self, **kwargs):
        context = super(MostWatched, self).get_context_data(**kwargs)
        context['list_title'] = 'Most Watched'
        return context


class RecentlyAdded(ListView):
    model = Movie
    paginate_by = 8
    ordering = ['-created']
    template_name = 'movie/movie_list.html'

    def get_context_data(self, **kwargs):
        context = super(RecentlyAdded, self).get_context_data(**kwargs)
        context['list_title'] = 'Recently Added'
        return context


class TopRated(ListView):
    model = Movie
    paginate_by = 8
    ordering = ['-rating']
    template_name = 'movie/movie_list.html'

    def get_context_data(self, **kwargs):
        context = super(TopRated, self).get_context_data(**kwargs)
        context['list_title'] = 'Top Rated'
        return context
