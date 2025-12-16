from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    # we can list all of our urls for our website here.. we will first start with the index or homepage
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>", views.post_detail, name="post_detail"),
    path("post/new", views.post_new, name="post_new"),
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("drafts/", views.post_draft_list, name="post_draft_list"),
    path("post/<int:pk>/publish/", views.post_publish, name="post_publish"),
    path("post/<int:pk>/remove", views.post_remove, name="post_remove"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("post<int:pk>/comment/", views.add_comment_to_post, name="add_comment_to_post"),
]

