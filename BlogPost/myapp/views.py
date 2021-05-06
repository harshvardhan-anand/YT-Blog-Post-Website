from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailForm, CommentForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def post_list(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 10)
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
    emailform = EmailForm()
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        print(request.POST)
        emailform = EmailForm(request.POST)
        if emailform.is_valid():
            cd = emailform.cleaned_data
            print(cd)
            name = cd['name']
            to = cd['to']
            message = cd['comment']
            subject = f"Shared post by {name}"
            senders_email = settings.EMAIL_HOST_USER

            send_mail(
                subject, 
                message,
                senders_email,
                [to]
            )

            return HttpResponseRedirect(reverse('myapp:detailview', args=[pk]))
    return render(request, 'myapp/detail.html', {
        'post':post, 
        'emailform':emailform,
        'comments':comments
    })


def comment_view(request, pk):
    commentform = CommentForm()
    if request.method=='POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            cd = commentform.cleaned_data
            print(cd)
            new_comment = commentform.save(commit=False)
            new_comment.post = Post.objects.get(pk=pk)
            new_comment.save()
        return HttpResponseRedirect(reverse('myapp:detailview', args=[pk]))
    return render(request, 'myapp/comment.html', {'commentform':commentform})