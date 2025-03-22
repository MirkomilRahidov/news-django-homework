from django.contrib import admin
from .models import CustomUser,Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'user', 'post')
