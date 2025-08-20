from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.

def index(request):
    books_obj = Book.objects.all().order_by("-rating")  # This line fetches ordered Book objects from the database and not order in python
    
    return render(request, 'book_outlet/index.html', {
        "books": books_obj,
        "total_books": books_obj.count(),
        "avg_rating": books_obj.aggregate(Avg('rating'))    # Aggregate returrns a dictionary with all aggregate functions
    })    
    # book_outlet/index.html is the path to template to be rendered
    # books_obj is passed to the template as "books" context variable


def book_detail(request, slug):
    # try:
    # except Book.DoesNotExist:
    #     book_obj = Book.objects.get(pk=id) # pk = primary key  
    #     raise Http404("Book not found")

    book_obj = get_object_or_404(Book, slug=slug)  
    return render(request, 'book_outlet/book_detail.html', {
        "book": book_obj  })
    
    