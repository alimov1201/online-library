from django.contrib import admin
from book.models import Category, Genre, Book

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Book)
