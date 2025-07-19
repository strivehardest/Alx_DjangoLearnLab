from django.contrib.auth import login  # ✅ required
from django.contrib.auth import logout  # ✅ optional but common
from django.contrib.auth.forms import UserCreationForm  # ✅ required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # ✅ using built-in login
            return redirect('member_view')  # or any other page
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)  # ✅ using built-in logout
    return render(request, 'relationship_app/logout.html')

# In views.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View to display a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

@user_passes_test(lambda u: u.is_authenticated and hasattr(u, 'userprofile') and u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda u: u.is_authenticated and hasattr(u, 'userprofile') and u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda u: u.is_authenticated and hasattr(u, 'userprofile') and u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

