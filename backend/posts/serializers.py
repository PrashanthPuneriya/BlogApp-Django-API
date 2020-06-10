from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'content')
        model = Post


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'content',
                  'created_at', 'updated_at', 'author')
        model = Post
