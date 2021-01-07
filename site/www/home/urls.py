from django.urls import path, re_path
from . import views
import articles

urlpatterns = [
        path("", views.homepage),
        re_path("(?P<pagename>(about|contribute))/", views.homepage, name="homepage"),
        ]
