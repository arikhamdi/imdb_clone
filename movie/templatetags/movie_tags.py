from django import template
import datetime

from movie.models import Movie, Banner


register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
