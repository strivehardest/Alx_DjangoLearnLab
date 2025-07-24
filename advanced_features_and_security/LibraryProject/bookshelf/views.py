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
