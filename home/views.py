from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, News
from datetime import date
from .forms import ContactMessageForm,CommentForm
from users.models import Comment
def home(request):
    categories = Category.objects.all() 
    latest_news = News.objects.order_by('-created_at')[:5]
    slider_news = News.objects.order_by('-created_at')[:3]
    latest_posts = News.objects.order_by('-created_at')[:6]
    popular_posts = News.objects.order_by('-views')[:2] 
    
    context = {
        'categories': categories,
        'latest_news': latest_news,
        'slider_news': slider_news,
        'latest_posts': latest_posts,
        'popular_posts': popular_posts,
        'current_date': date.today(),
    }
    
    return render(request, 'index.html', context)

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    comments = Comment.objects.filter(post=news).order_by('-created_at') 

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = news  
            comment.user = request.user  
            comment.save()
            return redirect('news_detail', id=id) 

    else:
        form = CommentForm()

    return render(request, 'single_page.html', {
        'news': news,
        'comments': comments,
        'form': form
    })

def category_info(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category_news = News.objects.filter(category=category).order_by('-created_at')
    popular_posts = News.objects.order_by('-views')[:5]
    context = {
        'category': category,
        'category_news': category_news,
        'popular_posts': popular_posts,
    }
    return render(request, 'c_details.html', context)

def contact_view(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactMessageForm()
    return render(request, 'contact.html', {'form': form})
