from django.views import generic
from django.shortcuts import render

# Create your views here.
from .models import Book, Author, Instance

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = Instance.objects.all().count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
class BookListView(generic.ListView):
    model=Book
    paginate_by = 10
class BookDetailView(generic.DetailView):
    model=Book
class AuthorListView(generic.ListView):
    model=Author
class AuthorDetailView(generic.DetailView):
    model=Author