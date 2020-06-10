from django.urls import path
from .views import PostListAllView, PostDetailView

urlpatterns = [
    # get -> list all posts
    path('', PostListAllView.as_view(), name='post-list-all'),
    
    # get -> list all user posts
    # path('my-posts/', PostListUserView.as_view(), name='post-list-user'),

    path('<int:id>/', PostDetailView.as_view(), name='post-detail'),
]
