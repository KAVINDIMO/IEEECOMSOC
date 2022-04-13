from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path("",views.Home,name="Home"),
path("event/",views.Events,name="Event"),
path("posts/",views.PostView,name="posts"),
path("blog/",views.BlogView,name="blog"),
path("post_upload/",views.post_upload,name="post_upload"),
path("blog_upload/",views.blog_upload,name="post_upload")
]