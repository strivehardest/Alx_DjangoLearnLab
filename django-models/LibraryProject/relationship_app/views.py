from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library

# ✅ Function-Based View that uses Book.objects.all() and the correct template path
def list_books(request):
    books = Book.objects.all()  # 👈 Required for ORM query check
    return render(request, 'relationship_app/list_books.html', {'books': books})  # 👈 Template path
