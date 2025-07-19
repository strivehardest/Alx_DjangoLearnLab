from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book  # Keep this if needed
from .models import Library  # 👈 Required explicitly

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View to display a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
