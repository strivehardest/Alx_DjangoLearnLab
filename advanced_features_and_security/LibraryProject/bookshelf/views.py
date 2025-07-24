from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from django.http import HttpResponse, HttpResponseForbidden

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author, user=request.user)
        return HttpResponse("Book created.")
    return render(request, 'bookshelf/book_form.html')

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return HttpResponse("Book updated.")
    return render(request, 'bookshelf/book_form.html', {'book': book})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return HttpResponse("Book deleted.")

# ✅ Safe ORM query
books = Book.objects.filter(title__icontains=search_query)

from .forms import BookForm

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return HttpResponse("Book created.")
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})
