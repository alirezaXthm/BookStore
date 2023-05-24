from django.shortcuts import render
from django.views import generic

from .models import Book

class BookListView(generic.ListView):
    model = Book
    template_name = 'book/book_list_view.html'    
    context_object_name = 'books'