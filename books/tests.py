#books/tests.py
from django.test import TestCase
from django.urls import reverse

from .models import Book

# Create your tests here.

class BookTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.book = Book.objects.create(
      title='Harry Potter',
      subtitle = "And the Chamber of Secrets",
      author = "J.K. Rowling",
      isbn = "9780439064873",
    )
    
    def test_book_content(self):
      self.assertEqual(f'{self.book.title}', 'Harry Potter')
      self.assertEqual(f'{self.book.subtitle}', 'And the Chamber of Secrets')
      self.assertEqual(f'{self.book.author}', 'J.K. Rowling')
      self.assertEqual(f'{self.book.isbn}', '9780439064873')
      
    def test_book_listview(self):
      response = self.client.get(reverse('home'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, 'Harry Potter')
      self.assertTemplateUsed(response, 'book_list.html')
    
    