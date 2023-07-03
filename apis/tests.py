from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book
# Create your tests here.


class APITests(APITestCase):
  @classmethod
  def setUpTestData(cls):
    cls.book = Book.objects.create(
      title = 'The Great Gatsby',
      subtitle = 'The Great Gatsby subtitle',
      author = 'William S. Vincent',
      isbn = '978-3-16-148410-0',
    ) 

  def test_api_listview(self):
    response = self.client.get(reverse('book_list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertContains(response, self.book.title)
    self.assertContains(response, self.book.author)
    self.assertContains(response, self.book.subtitle)
    self.assertContains(response, self.book.isbn)