from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from forum.models import User as ForumUser

def index(request):
  return render(request, 'home/index.html')

def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      auth_user = form.save()
      ForumUser.objects.create(
        auth_user=auth_user,
        name=auth_user.username,
        date_joined=timezone.now()
      )
      login(request, auth_user)
      return redirect('index')
    else:
      return render(request, 'registration/register.html', {'form': form})
  else:
    form = UserCreationForm()
  return render(request, 'registration/register.html', {'form': form})
