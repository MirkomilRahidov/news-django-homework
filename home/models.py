# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    short_description = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)  
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']