from django.urls import path
from .views import PostListAll, PostListCreateUser

urlpatterns = [
    # get -> list all posts
    path('', PostListAll.as_view(), name='post-list-all'),
    
    # get -> list all user posts || post -> create a post
    path('post/', PostListCreateUser.as_view(), name='post-list-create-user'),

]
