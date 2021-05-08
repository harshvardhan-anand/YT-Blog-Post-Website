from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'myapp'

urlpatterns = [
    path("list/", views.post_list, name='listview'),
    path("detail/<int:pk>", views.post_detail, name='detailview'),
    path('<int:pk>/comment', views.comment_view, name='commentview'), 
    path('feed/', LatestPostsFeed(), name='latest_feed')
]
