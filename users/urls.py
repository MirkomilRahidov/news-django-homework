from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterView,LoginView,LogoutView,ProfileView,profileupdate,CommentUpdateView
app_name = 'users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profileupdate/', profileupdate, name='profile_update'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
