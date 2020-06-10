from django.urls import path
from .views import (
    PostAllView,
    deleteAllPostsView,
    PostUserView,
    PostDetailView,
)


urlpatterns = [
    # list all posts
    path('', PostAllView.as_view(), name='post-all'),

    path('<int:id>/', PostDetailView.as_view(), name='post-detail'),

    # create a post, list/delete all user posts
    path('post/', PostUserView.as_view(), name='post-user'),

    path('delete-all-posts/', deleteAllPostsView, name='delete-all-posts'),
]
