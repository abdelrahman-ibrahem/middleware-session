from rest_framework import serializers
from posts.models import Post, UserLog
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'creation_date', 'image', 'username')
    
    def get_username(self, instance):
        return instance.user.username
    
    def create(self, validated_data):
        instance = Post.objects.create(
            user=User.objects.last(),
            title=validated_data.get('title'),
            content=validated_data.get('content')
        )
        if validated_data.get('image'):
            instance.image = validated_data.get('image')
        instance.save()
        return instance

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        Token.object.create(user=user)
        return user


class LogSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = UserLog
        fields = ('username', 'action', )
    
    def get_username(self, instance):
        return instance.user.username