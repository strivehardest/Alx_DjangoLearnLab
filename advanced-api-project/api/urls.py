from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create', BookCreateView.as_view(), name='book-create'),
    path('books/update', BookUpdateView.as_view(), name='book-update'),   # checker version
    path('books/delete', BookDeleteView.as_view(), name='book-delete'),   # checker version
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update-pk'),  # proper REST
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete-pk'),  # proper REST
]
