from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import PostViewSet

api_router = DefaultRouter()
api_router.register(r'posts', PostViewSet)

urlpatterns = [
  path("", views.index, name="index"),
  path("post/<int:post_id>", views.post, name="post"),
  path("api/", include(api_router.urls)),
]
