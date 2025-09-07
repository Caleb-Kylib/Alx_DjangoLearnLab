from django.contrib import admin
from .models import Book

# Custom admin class to control how Book appears in the admin
class BookAdmin(admin.ModelAdmin):
    # Columns to show in the book list
    list_display = ('title', 'author', 'publication_year')
    
    # Add a search box to find books by title or author
    search_fields = ('title', 'author')
    
    # Add a filter sidebar to filter by publication year
    list_filter = ('publication_year',)

# Register the Book model using the custom admin class
admin.site.register(Book, BookAdmin)

