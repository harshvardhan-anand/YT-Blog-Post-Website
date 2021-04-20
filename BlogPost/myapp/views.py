from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_list(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 1)
    print(request.GET)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "myapp/homepage.html", context={'posts':posts})

def post_detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'myapp/detail.html', {'post':post})