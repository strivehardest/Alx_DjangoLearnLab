from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='posts'),       # blog posts listing
    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]

from django.contrib import admin
from django.urls import path
from blog import views  # adjust to your app name

from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('comments/<int:pk>/edit/', views.edit_comment, name='edit_comment'),
    path('comments/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]

from django.urls import path
from . import views

urlpatterns = [
    # Existing post URLs
    path('', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    # Comment URLs (required by the check)
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    # existing paths...

    # Tag & Search
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'),
    path('search/', views.search_posts, name='search-posts'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_posts, name='search_posts'),  # ✅ search
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),  # ✅ tag filter
]

from django.urls import path
from .views import PostByTagListView

urlpatterns = [
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]

from django.urls import path
from .views import PostListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
]

path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),


