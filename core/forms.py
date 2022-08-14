
from .models import Book, Author, Instance, Member
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
        model = Instance
        fields=['book', 'borrower','return_date']
        widgets = {
            'return_date': DateInput(attrs={'min':f'{datetime.datetime.now().date()}'}),
        }
from dal import autocomplete
class charinput(forms.CharField):
    pass
class GetInstance(forms.ModelForm):
    s=AddBookForm()
    class Meta:
        model = Instance
        fields = ['id']
        widgets = {
            's': autocomplete.ModelSelect2(url='get_instance'),
            
        }

class ReturnBookForm(autocomplete.FutureModelForm):
    class Meta:
        model=Instance
        
        fields=['book']
        autocomplete_fields=['book']
        #autocomplete_names = {'book': 'GetInstance'}
        # exclude = ()
        widgets = {
             'book': GetInstance()
         }
