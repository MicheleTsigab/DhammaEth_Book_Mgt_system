from django.views import generic
from django.shortcuts import render

from core.forms import AddBookForm,AddAuthorForm,AddMemberForm, LendBookForm, ReturnBookForm
from django.urls import reverse_lazy
# Create your views here.
from .models import Book, Author, BorrowedBook, Instance, Member

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = Instance.objects.all().count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context=context)
class BookListView(generic.ListView):
    model=Book
    paginate_by = 10
class BookDetailView(generic.DetailView):
    model=Book
class InstanceDetailView(generic.DetailView):
    model=Instance
class AuthorListView(generic.ListView):
    model=Author
class AuthorDetailView(generic.DetailView):
    model=Author
class AddBookView(generic.CreateView):
    model=Book
    form_class = AddBookForm
    template_name = 'core/add_book.html'
    success_url = reverse_lazy('index')
class AddAuthorView(generic.CreateView):
    model=Author
    form_class = AddAuthorForm
    template_name='core/add_author.html'
    success_url=reverse_lazy('index')
class LendBookView(generic.CreateView):
    model=BorrowedBook
    form_class=LendBookForm
    template_name='core/lend_book.html'
    success_url=reverse_lazy('index')
class AddMemberView(generic.CreateView):
    model=Member
    form_class=AddMemberForm
    template_name='core/add_member.html'
    success_url=reverse_lazy('index')
class ReturnBookView(generic.ListView):
    #Should change this view to update view if lending history is a functional requirement
    model=BorrowedBook
    form_class=ReturnBookForm
    template_name='core/return_book.html'
    success_url=reverse_lazy('index')