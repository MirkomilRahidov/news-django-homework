from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from home.models import News
class CustomUser(AbstractUser, PermissionsMixin):
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, default='avatars/default.png')
    address = models.CharField(max_length=200, blank=True,null=True)

    def __str__(self):
        return self.username
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Comment by {self.user} at {self.created_at}"