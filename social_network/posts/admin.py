from django.contrib import admin
from .models import Post, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['text', 'user', 'created_at']
    search_fields = ['text', 'user__username']
    list_filter = ['created_at', 'user']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'post', 'user', 'created_at']
    search_fields = ['text', 'user__username']
    list_filter = ['created_at', 'user']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user']
    list_filter = ['user']