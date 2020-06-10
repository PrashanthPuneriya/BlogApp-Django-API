from rest_framework import views, response, status, permissions

from .models import Post
from .serializers import PostSerializer

class PostListAll(views.APIView):
    # List all posts
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return response.Response(data={'posts': serializer.data}, status=status.HTTP_200_OK)

# class PostListUser(views.APIView):
    
#     def get(self, request):
#         # Lists all the posts of the user
#         qs = Post.objects.all().filter(author=request.user)
#         serializer = PostSerializer(qs, many=True)
#         return response.Response(data={'posts': serializer.data}, status=status.HTTP_200_OK)    

class PostDetail(views.APIView):
    
    def get(self, request, id):
        # Detail view of the post
        pass

    def post(self, request):
        # Create a post
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

    