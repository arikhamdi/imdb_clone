from django.urls import path
from .views import MovieList, MovieDetail, MostWatched

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('most_watched', MostWatched.as_view(), name='most_watched'),
    path('recently_added', MostWatched.as_view(), name='recently_added'),
    path('top_rated', MostWatched.as_view(), name='top_rated'),
]
