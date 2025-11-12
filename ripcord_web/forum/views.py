from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
  posts = Post.objects.all().order_by('-date')
  return render(request, 'forum/index.html', {'posts': posts})

def post(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  return render(request, 'forum/post.html', {'post': post})

