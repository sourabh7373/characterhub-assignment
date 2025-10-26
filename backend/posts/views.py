from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .pagination import PostCursorPagination

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostCursorPagination
