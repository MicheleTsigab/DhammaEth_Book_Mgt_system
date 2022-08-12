from xmlrpc.client import DateTime
from .models import Book, BorrowedBook, Author, Member
from django import forms
import datetime
class AddBookForm(forms.ModelForm):    
    class Meta:
        model = Book
        fields='__all__'
    #     fields = ['name', 'date', 'members']    
    # name = forms.CharField()
    # date = forms.DateInput()    
    # members = forms.ModelMultipleChoiceField(
    # queryset=Member.objects.all(),
    # widget=forms.CheckboxSelectMultiple
    # )
class AddAuthorForm(forms.ModelForm):    
    class Meta:
        model = Author
        fields='__all__'
class AddMemberForm(forms.ModelForm):    
    class Meta:
        model = Member
        fields=['dhamma_id','first_name','last_name','phone','email']
class DateInput(forms.DateInput):
    input_type = 'date'
class LendBookForm(forms.ModelForm):  
      
    class Meta:
        model = BorrowedBook
        fields=['book', 'borrower','return_date']
        widgets = {
            'return_date': DateInput(attrs={'min':f'{datetime.datetime.now().date()}'}),
        }
from searchableselect.widgets import SearchableSelect
class ReturnBookForm(forms.ModelForm):
    class Meta:
        model=BorrowedBook
        fields=['book']
        exclude = ()
        widgets = {
            'Book_Instance': SearchableSelect(model='Instance', search_field='book', limit=10)
        }
