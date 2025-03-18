from django.urls import path
from .views import home,news_detail,category_info

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:id>', news_detail, name='news_detail'),
    path('category/<int:category_id>', category_info, name='category_info'),
]