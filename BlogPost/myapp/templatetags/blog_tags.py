from ..models import Post
from django import template

register = template.Library()

@register.simple_tag
def total_post():
    return Post.objects.count()


@register.inclusion_tag('myapp/show_latest_post.html')
def show_latest_posts(count=3):
    latest_posts = Post.objects.filter(status='published').order_by('-created')[:count]
    return {
        'latest_posts':latest_posts
    }