from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name="Author One")

        # Create sample books
        self.book1 = Book.objects.create(
            title="Book One",
            author=self.author,
            publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            author=self.author,
            publication_year=2021
        )

        self.book_list_url = reverse('book-list')  # From your router
        self.book_detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_list_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Book One', str(response.data))

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2023
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Should Fail",
            "author": self.author.id,
            "publication_year": 2023
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2022
        }
        response = self.client.put(self.book_detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        response = self.client.get(self.book_list_url, {'title': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['title'] == 'Book One' for book in response.data))

    def test_search_books_by_title(self):
        response = self.client.get(self.book_list_url, {'search': 'Book Two'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Book Two' in book['title'] for book in response.data))

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.book_list_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
