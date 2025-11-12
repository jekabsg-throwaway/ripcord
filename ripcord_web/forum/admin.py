from django.contrib import admin

from .models import School, User, Post, Comment

admin.site.register(School)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
