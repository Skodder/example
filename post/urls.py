from django.conf.urls import include, url 
from django.contrib import admin
from post.views import PostListView

urlpatterns = [
    url(r"^posts/", PostListView.as_view(), name="post_list")
]

