from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from posts.models import Post, UserLog
from posts.serializers import PostSerializer, LogSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from posts.permissions import IsAuthor


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

class LogList(generics.ListAPIView):
    queryset = UserLog.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.AllowAny]

class PostDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthor]

# user = User.objects.get(id=1)
# user.is_superuser
# function based views vs class based views 
@api_view(['GET'])
@permission_classes([
    permissions.IsAuthenticated
])
def post_list(request):
    posts = Post.objects.all()
    posts = PostSerializer(posts, many=True)
    return Response(posts.data, status=status.HTTP_200_OK)


from rest_framework import serializers
class OtherPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_post(request):
    title = request.data.get('title')
    content = request.data.get('content')
    image = request.data.get('image')
    instance = Post.objects.create(
        user=request.user,
        title=title,
        content=content
    )
    if image:
        instance.image = image
    instance.save()
    return Response(PostSerializer(instance).data, status=status.HTTP_201_CREATED)
    # serializer = PostSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data)
    # else:
    #     return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([
    IsAuthor,
    permissions.IsAuthenticated,
])
def update_post(request):
    post_id = request.data.get('post_id')
    title = request.data.get('title')
    content = request.data.get('content')
    image = request.data.get('image')

    post = Post.objects.get(id=post_id)

    if title:
        post.title = title
    if content:
        post.content = content
    if image:
        post.image = image
    post.save()
    return Response(PostSerializer(post).data, status=status.HTTP_200_OK)


@api_view(['POST'])
def delete_post(request):
    post_id = request.data.get('post_id')
    Post.objects.get(id=post_id).delete()
    return Response({
        'message': 'Post is deleted'
    })
