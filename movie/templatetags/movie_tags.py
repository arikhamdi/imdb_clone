from django import template
import datetime

from movie.models import Movie, Banner, Category


register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.inclusion_tag('base.html')
def show_list_category():
    # list_of_categories = Movie.category.all()
    list_of_categories = Category.objects.all()
    return {'list_of_categories': list_of_categories}
