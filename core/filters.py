
import django_filters
from django import forms
from .models import  Book, Instance
class DateInput(forms.DateInput):
    input_type = 'date'

class InstanceFilter(django_filters.FilterSet):
    book__title=django_filters.CharFilter(
        label="Book Title",
        lookup_expr='icontains')
    borrower__first_name=django_filters.CharFilter(
        label='First Name',
        lookup_expr='icontains')
    borrower__last_name=django_filters.CharFilter(
        label='Last Name',
        lookup_expr='icontains')
    borrowed_date=django_filters.DateFilter(widget=DateInput())
    class Meta:
        model=Instance
        
        fields={'id':['exact']}
class AvailableBooksFilter(django_filters.FilterSet): 
    book__title=django_filters.CharFilter(
        label="Book Title",
        lookup_expr='icontains',
        )
    class Meta:
        model = Instance
        fields = ['book__title']
class BookFilter(django_filters.FilterSet):
    search=django_filters.CharFilter(field_name='title',lookup_expr='icontains')
    class Meta:
        model=Book
        fields=['search'] 