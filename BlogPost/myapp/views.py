from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_list(request):
    all_posts = Post.objects.all()
    return render(request, "myapp/homepage.html", context={'posts':all_posts})

def post_detail(request, pk):
    post = Post.objects.get(pk = pk)
    return render(request, 'myapp/detail.html', {'post':post})