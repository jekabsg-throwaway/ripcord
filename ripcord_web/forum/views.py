from django.shortcuts import render
from .models import Post

def index(request):
  posts = Post.objects.all().order_by('-date')
  return render(request, 'forum/index.html', {'posts': posts})
