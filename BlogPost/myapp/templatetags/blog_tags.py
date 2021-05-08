from ..models import Post
from django import template

register = template.Library()

@register.simple_tag
def total_post():
    return Post.objects.count()