from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.post_list, name='listview')
]
