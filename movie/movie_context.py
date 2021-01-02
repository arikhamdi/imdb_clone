from .models import Movie, Category


def get_categories(self):
    return {'categories': Category.objects.all()}


def get_release_years(self):
    movies = Movie.objects.order_by('-release_date')
    years = []
    for movie in movies:
        if movie.release_date.year not in years:
            years.append(movie.release_date.year)
    return {'years': years[:10]}
