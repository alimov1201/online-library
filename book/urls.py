from django.urls import path
from book.views import main, book_detail, create_book, update_book, delete_book, category_page, search_page

urlpatterns = [
    path('', main, name='home'),
    path('book_detail/<int:id>', book_detail, name='book_detail'),
    path('create_book/', create_book, name='create'),
    path('update_book/<int:id>/', update_book, name='update'),
    path('delete_book/<int:id>/', delete_book, name='delete'),
    path('category_page/', category_page, name='category'),
    path('search_page/', search_page, name='search')
]