from django.urls import path
from .views import PostListAll

urlpatterns = [
    # get -> list all posts
    path('', PostListAll.as_view(), name='post-list-all'),
    # get -> list all user posts
    # path('my-posts/', PostListUser.as_view(), name='post-list-user'),

    
]
