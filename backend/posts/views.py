from rest_framework import views, response, status, permissions

from .models import Post
from .serializers import PostSerializer

class PostListAll(views.APIView):
    # List all posts
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return response.Response(data={'posts': serializer.data}, status=status.HTTP_200_OK)

class PostListCreateUser(views.APIView):
    # Lists all the posts of the user

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return response.Response(data={'posts': serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        json_data = self.request.data
        post_data = json_data['post']
        de_serializer = PostSerializer(data=post_data)
        try:
            if de_serializer.is_valid(raise_exception=True):
                de_serializer.save(author=request.user)
                return response.Response(data={'success': 'Post has been created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return response.Response(data={'error': de_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    