from django.urls import path
from . import views

urlpatterns = [
        path("post-comment", views.post_comment, name="post_comment"),
        path("", views.articles_home, name="articles_home"),
        path("<path:filename>", views.articles_home, name="articles"),

        ]
