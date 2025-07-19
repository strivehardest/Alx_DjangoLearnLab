import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # ✅ Query all books by a specific author using filter
    author_name = "Chinua Achebe"
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Required line
        print(f"\nBooks by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name '{author_name}'")

    # ✅ List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library.name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name '{library_name}'")

    # ✅ Retrieve the librarian for a library using .get(library=...)
    try:
        librarian = Librarian.objects.get(library=library)  # Required line
        print(f"\nLibrarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}")

if __name__ == "__main__":
    run_queries()
