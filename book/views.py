from django.shortcuts import render, get_object_or_404, redirect
from book.models import Book, Category, Genre
from book.forms import BookForm

def main(request):
    new_books = Book.objects.order_by('-created_date')
    popular_books = Book.objects.order_by('-views')[:3]
    genres = Genre.objects.all()
    context = {
        'new_books': new_books,
        'genres': genres,
        'popular_books':popular_books,
    }
    return render(request, 'index.html', context=context)


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    genres = Genre.objects.all()
    if request.user.is_authenticated and request.user not in book.users.all():
        book.views += 1
        book.users.add(request.user)
        book.save()
    context = {
        'genres': genres,
        'book': book
    }
    return render(request, 'book-detail.html', context=context)

def category_page(request):
    genres = Genre.objects.all()
    genre = request.GET.get('genre')
    category = request.GET.get('category')
    if genre:
        books = Book.objects.filter(genre__name__icontains=genre)
    elif category:
        books = Book.objects.filter(category__name__icontains=category)
    else:
        books = Book.objects.all()

    context = {
        'books': books,
        'genre': genre,
        'category': category,
        'genres': genres,
    }
    return render(request, 'category.html', context=context)

def search_page(request):
    genres = Genre.objects.all()
    search = request.GET.get('search')
    if search:
        books = Book.objects.filter(title__icontains=search)
    else:
        books = Book.objects.all()
    
    context = {
        'books': books,
        'search': search,
        'genres': genres,
    }
    return render(request, 'search.html', context=context)

def create_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'create.html', context=context)

def update_book(request, id):
    book = get_object_or_404(Book.objects.all(), id=id)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(data=request.POST, files=request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'update.html', context=context)

def delete_book(request, id):
     book = get_object_or_404(Book.objects.all(), id=id)
     if request.method == 'POST':
         book.delete()
         return redirect('home')
     return render(request, 'delete.html')