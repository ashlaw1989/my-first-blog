from django.urls import path
from . import views


urlpatterns = [
    # we can list all of our urls for our website here.. we will first start with the index or homepage
    path("", views.post_list, name="post_list"),
]

