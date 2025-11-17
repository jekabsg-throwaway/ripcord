from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer

def index(request):
  posts = Post.objects.all().order_by('-date')
  return render(request, 'forum/index.html', {'posts': posts})

def post(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  comments = Comment.objects.filter(post=post)
  return render(request, 'forum/post.html', {'post': post, 'comments': comments})

class PostViewSet (viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
