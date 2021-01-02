from django.urls import path
from .views import (
    MovieList,
    MovieDetail,
    MostWatched,
    RecentlyAdded,
    TopRated,
    ActorDetail,
    MovieCategory,
    MovieLanguage,
    MovieSearch,
    MovieYearList)

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('movie/<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('year/<int:year>', MovieYearList.as_view(), name='movie_year'),
    path('most_watched', MostWatched.as_view(), name='most_watched'),
    path('recently_added', RecentlyAdded.as_view(), name='recently_added'),
    path('top_rated', TopRated.as_view(), name='top_rated'),

    path('search/', MovieSearch.as_view(), name='movie_search'),

    path('actor/<slug:slug>', ActorDetail.as_view(), name='actor_detail'),

    path('category/<str:name>', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
]
