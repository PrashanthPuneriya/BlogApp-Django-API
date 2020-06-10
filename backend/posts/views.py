from rest_framework import views, response, status, permissions

from .models import Post
from .serializers import PostSerializer


class PostListAllView(views.APIView):
    # List all posts
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return response.Response(data={'posts': serializer.data}, status=status.HTTP_200_OK)

# class PostListUserView(views.APIView):

#     def get(self, request):
#         # Lists all the posts of the user
#         qs = Post.objects.all().filter(author=request.user)
#         serializer = PostSerializer(qs, many=True)
#         return response.Response(data={'posts': serializer.data}, status=status.HTTP_200_OK)


class PostDetailView(views.APIView):

    def get(self, request, post_id):
        # Detail view of the post
        try:
            post = Post.objects.get(pk=post_id)
            serializer = PostSerializer(data=post)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return response.Response(None, status=status.HTTP_404_NOT_FOUND)

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

    def patch(self, request, post_id):
        # PATCH -> Because we are updating only certain fields of the post but not the entire entity
        try:
            post = Post.objects.get(pk=post_id)
            serializer = PostSerializer(instance=post, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return response.Response(data={'success': 'Post has been updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return response.Response(data={'error': 'Some error has occured'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
            post.delete()
            return response.Response(data={'success': 'Post has been deleted successfully'}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return response.Response(None, status=status.HTTP_400_BAD_REQUEST)
