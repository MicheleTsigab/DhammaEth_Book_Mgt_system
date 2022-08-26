from django.db.models import Q
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from .filters import InstanceFilter,AvailableBooksFilter,BookFilter
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
class AddInstanceView(LoginRequiredMixin,generic.FormView):
    model=Instance
    form_class=MultipleInstance
    template_name='core/add_model_partial.html'
class AddBookView(LoginRequiredMixin,generic.CreateView):
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
class AddAuthorView(LoginRequiredMixin,generic.CreateView):
    model=Author
    form_class = AddAuthorForm
    template_name='core/add_model_partial.html'
    success_url=reverse_lazy('index')

class AddMemberView(LoginRequiredMixin,generic.CreateView):
    model=Member
    form_class=AddMemberForm
    template_name='core/add_member.html'
    success_url=reverse_lazy('index')
class AddLanguageView(LoginRequiredMixin,generic.CreateView):
    model=Language
    form_class=AddLanguageForm
    template_name='core/add_model_partial.html'
    success_url=reverse_lazy('index')
class InstanceFilterView(FilterView):
    model = Instance    
    template_name = 'core/instance_list.html' 
    filterset_class = InstanceFilter
    
class BookFilterView(FilterView):
    model = Book    
    template_name = 'core/book_list.html' 
    filterset_class = BookFilter
    context_object_name="book_list"
    paginate_by=10
class AvailableBookView(LoginRequiredMixin,FilterView):
    queryset=Instance.objects.filter(borrower=None,borrowed_date=None)
    model=Instance
    filterset_class=AvailableBooksFilter
    template_name='core/available_books.html'
    context_object_name = "instances"
    paginate_by=10
class BorrowedBookView(LoginRequiredMixin,FilterView):
    model=Instance
    queryset=Instance.objects.filter(Q(borrower__isnull=False)|Q(borrowed_date__isnull=False))
    filterset_class=InstanceFilter
    template_name='core/borrowed_books.html'
    context_object_name = "instances"
    paginate_by=10
class LendInstance(LoginRequiredMixin,generic.UpdateView):
    model=Instance
    form_class=LendBookForm
    template_name='core/lend_book.html'

@login_required
def ReturnInstance(request,pk):
   instance=get_object_or_404(Instance, pk=pk)
   instance.borrower=None
   instance.borrowed_date=None
   instance.return_date=None
   instance.save()
   context={
    'instance':instance,
    'status':'returned'
   }
   return render(request, 'core/instance_detail.html', context=context)
