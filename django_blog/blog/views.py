# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, ProfileForm
from .models import Post

def home(request):
    posts = Post.objects.select_related('author').order_by('-published_date')[:10]
    return render(request, 'blog/home.html', {'posts': posts})

def register(request):
    if request.user.is_authenticated:
        return redirect('blog:home')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # immediate login after registration
            messages.success(request, f'Welcome, {user.username}! Your account was created.')
            return redirect('blog:home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'blog/logout.html'

@login_required
def profile(request):
    user = request.user
    profile = getattr(user, 'profile', None)
    if request.method == 'POST':
        pform = ProfileForm(request.POST, request.FILES, instance=profile)
        if pform.is_valid():
            pform.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('blog:profile')
        else:
            messages.error(request, 'Please fix the errors below.')
    else:
        pform = ProfileForm(instance=profile)
    return render(request, 'blog/profile.html', {'pform': pform})

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', pk=comment.post.pk)
    return render(request, 'blog/delete_comment.html', {'comment': comment})
