from rest_framework import views, response, status, permissions

from rest_framework.decorators import api_view, permission_classes

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


class PostAllView(views.APIView):
    # List all posts
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return response.Response(data={"posts": serializer.data}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([permissions.IsAdminUser])
def deleteAllPostsView(self, request):
    Post.objects.all().delete()
    return response.Response(data={"success": "All posts has been deleted"}, status=status.HTTP_200_OK)

class PostUserView(views.APIView):

    def get(self, request):
        # Lists all the posts of the user
        qs = Post.objects.all().filter(author=request.user)
        serializer = PostSerializer(qs, many=True)
        return response.Response(data={"posts": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        # Create a post
        json_data = self.request.data
        post_data = json_data['post']
        de_serializer = PostSerializer(data=post_data)
        try:
            if de_serializer.is_valid(raise_exception=True):
                de_serializer.save(author=request.user)
                return response.Response(data={"success": "Post has been created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return response.Response(data={'error': de_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        Post.objects.all().filter(author=request.user).delete()
        return response.Response(data={"success": "All '{}' posts has been deleted".format(request.user.username)}, status=status.HTTP_200_OK)


class PostDetailView(views.APIView):

    def get(self, request, post_id):
        # Detail view of the post
        try:
            post = Post.objects.get(pk=post_id)
            serializer = PostDetailSerializer(post)
            # serializer = PostSerializer(post)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return response.Response(data={"error": "Post doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, post_id):
        # PATCH -> Because we are updating only certain fields of the post but not the entire entity
        try:
            post = Post.objects.get(pk=post_id)
            serializer = PostSerializer(instance=post, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return response.Response(data={"success": "Post has been updated successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return response.Response(data={"error": "Some error has occured"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
            post.delete()
            return response.Response(data={"success": "Post has been deleted successfully"}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return response.Response(data={"error": "Post doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
