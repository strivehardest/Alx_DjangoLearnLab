# relationship_app/urls.py

from django.urls import path
from .views import (
    login_view,
    logout_view,
    register_view,
    admin_view,
    librarian_view,
    member_view,
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('admin-dashboard/', admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view, name='member_view'),
]
