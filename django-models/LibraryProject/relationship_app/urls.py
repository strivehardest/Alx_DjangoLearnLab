from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # for views.register

urlpatterns = [
    # ✅ Django built-in class-based views for login/logout
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # ✅ Custom registration view
    path('register/', views.register, name='register'),
]


from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # FBV
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # CBV
]

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
]


