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


