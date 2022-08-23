from django.views import generic

from django.shortcuts import render,get_object_or_404
from .filters import InstanceFilter,AvailableBooksFilter
from core.forms import *
from django.urls import reverse_lazy
from .models import Book, Author, Instance, Language, Member
from django_filters.views import FilterView
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
class InstanceListView(generic.ListView):
    model=Instance

class InstanceDetailView(generic.DetailView):
    model=Instance
class AuthorListView(generic.ListView):
    model=Author
class AuthorDetailView(generic.DetailView):
    model=Author
### Creation Views
class AddInstanceView(generic.FormView):
    model=Instance
    form_class=MultipleInstance
    template_name='core/add_model_partial.html'


class AddBookView(generic.CreateView):
    model=Book
    form_class = AddBookForm
    template_name = 'core/add_book.html'
    def form_valid(self, form):
        num = form.cleaned_data['copies']
        res=super().form_valid(form)
        book=form.instance
        if num:
            num=int(num)
        for _ in range(num):
            Instance(book=book).save()
        return res
class AddAuthorView(generic.CreateView):
    model=Author
    form_class = AddAuthorForm
    template_name='core/add_model_partial.html'
    success_url=reverse_lazy('index')

class AddMemberView(generic.CreateView):
    model=Member
    form_class=AddMemberForm
    template_name='core/add_member.html'
    success_url=reverse_lazy('index')
class AddLanguageView(generic.CreateView):
    model=Language
    form_class=AddLanguageForm
    template_name='core/add_model_partial.html'
    success_url=reverse_lazy('index')
class InstanceFilterView(FilterView):
    model = Instance    
    template_name = 'core/instance_list.html' 
    filterset_class = InstanceFilter
class AvailableBookView(FilterView):
    model=Instance
    filterset_class=AvailableBooksFilter
    template_name='core/available_books.html'
class BorrowedBookView(FilterView):
    model=Instance
    filterset_class=InstanceFilter
    template_name='core/borrowed_books.html'
    
class LendInstance(generic.UpdateView):
    model=Instance
    form_class=LendBookForm
    template_name='core/lend_book.html'
# @loginrequired
def ReturnInstance(request,pk):
   instance=get_object_or_404(Instance, pk=pk)
   instance.borrower=None
   instance.borrowed_date=None
   instance.return_date=None
   context={
    'instance':instance,
    'status':'returned'
   }
   return render(request, 'core/instance_detail.html', context=context)
