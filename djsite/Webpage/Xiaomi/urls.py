from django.urls import include,path, re_path
from .views import *
import os

urlpatterns = [
    path("", index, name="home"),
    path("sm/", smartphone, name="sm"),
    re_path(r"^laptop/(?P<model>[0-9])/", laptop, name=r"^laptop/(?P<model>[0-9])"),
    path('about/', about_us, name="about_us"),
    path("others/", others ,name="Others"),
    path("leptops/", leptops, name= "Laptops"),
    path("add_text/", add_text, name="add_text"),
    path("feedback/", feed_back, name="feed_back"),
    path("login/", log_in, name="log_in")

]














