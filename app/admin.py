from django.contrib import admin
from app.models import Book, Author, Reader, Borrow_book

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(Borrow_book)
