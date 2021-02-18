from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path("list/", views.post_list, name='listview'),
    path("detail/<int:pk>", views.post_detail, name='detailview')
]
