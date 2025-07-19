from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library  # ✅ Required import

# ✅ Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()  # ✅ Required query
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ Required template path

# ✅ Class-Based View to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ Required template path
    context_object_name = 'library'  # ✅ Required context name
