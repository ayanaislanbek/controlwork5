from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment
from rest_framework.exceptions import ValidationError


class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField()

class UserAuthSerializer(UserBaseSerializer):
    pass

class UserCreateSerializer(UserBaseSerializer):

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError('user already exists')
        return username
    



class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = '__all__'



class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'title body is_published'.split()



class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = '__all__'



class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__' 



class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'body'.split()




