from django.shortcuts import render,redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Comment
from home.forms import CommentForm
from .forms import RegisterForm, LoginForm,ProfileUpdateForm
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'registration/register.html', {'form': form})
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
    def post(self, request):
        form =LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            user= authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            return render(request,'registration/login.html', {'form':form})
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
class ProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        form = ProfileUpdateForm(instance=request.user)
        user_comments = Comment.objects.filter(user=request.user).order_by('-created_at')

        return render(request, 'registration/profile.html', {
            'form': form,
            'comments': user_comments
        })
@login_required
def profileupdate(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')  
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "registration/profile_update.html", {"form": form})
class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'registration/comment_update.html'
    
    def get_success_url(self):
        return reverse_lazy('users:profile')

    def form_valid(self, form):
        comment = form.save(commit=False)
        if comment.user != self.request.user:
            return redirect('users:profile')  
        comment.save()
        return super().form_valid(form)
            
        
  
