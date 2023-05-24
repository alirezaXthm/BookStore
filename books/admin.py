from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'id']
    

admin.site.register(Book, BookAdmin)