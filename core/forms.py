
from .models import Book, Author, Instance, Language, Member
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Row,Column,Field,Button,Div,HTML
from crispy_forms.bootstrap import Modal
import core.urls

import datetime
from django.urls import reverse
class MultipleInstance(forms.Form):
    num_of_copies=forms.NumberInput()
class AddInstanceForm(forms.ModelForm):
    class Meta:
        model=Instance
        fields='__all__'  
class AddLanguageForm(forms.ModelForm):
    class Meta:
        model=Language
        fields='__all__'
class AddAuthorForm(forms.ModelForm): 
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper() 
        
        self.helper.layout = Layout(
            Row( 
            Field('first_name',css_class='form-control'),
            Field('last_name',css_class='from-control'),
            css_class='row'
            ))   
    class Meta:
        model = Author
        fields=['first_name','last_name']
class AddBookForm(forms.ModelForm):
    copies=forms.CharField(widget=forms.NumberInput())
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper(self) 
        self.helper.layout = Layout(
            Row(     
                Column(Field('title'),css_class='col-8 col-xl-8 '),
                Column(Field('author',css_class="form-control"),css_class='col-8 col-xl-8'),
                Column(
                    # This button below uses htmx-request to get an author 
                    # creation form and put it in a bootstrap modal body
                    #  so as to create author without refreshing the page
                HTML("<button type='button' class='btn btn-success mt-4' hx-get='{% url 'add-author'%}' hx-target='#add_author_form' data-bs-toggle='modal'data-bs-target='#addauthor' hx-swap='#add-author-form'>Add Author</button>")
                    ,css_class='col-4 col-xl-4'
                    ),
                Column(Field('cover',css_class='form-control'),css_class='col-8 col-xl-8 col-auto'),
                Column(Field('language',css_class='form-control'),css_class='col-8 col-xl-8 col-auto'),
                Column(HTML("<button type='button' class='btn btn-success mt-4' hx-get='{% url 'add-lang'%}' hx-target='#add_lang_form' data-bs-toggle='modal' data-bs-target='#addlang' hx-swap='#add_lang_form'>Add Language</button>")
                ,css_class='col-4 col-xl-4 col-auto'),
                # easy way to add book copies by specifying the number of copies
                Column(Field('copies', type='number', css_class='form-control',
                 placeholder='Enter number of Copies E.g 10'),
                 css_class='col-8 col-xl-8 col-auto'),
                Column(Submit('submit', 'Add Book', css_class='btn btn-primary mt-2'),css_class='col-12'),
                css_class='row align-items-center'
            ),       
        )
    class Meta:
        model = Book
        fields=['title','author','cover','language','copies']
        
class AddMemberForm(forms.ModelForm):    
    class Meta:
        model = Member
        fields=['dhamma_id','first_name','last_name','phone','email']
class DateInput(forms.DateInput):
    input_type = 'date'
class LendBookForm(forms.ModelForm):  
      
    class Meta:
        model = Instance
        fields=['book', 'borrower','return_date','borrowed_date']
        widgets = {
            'borrower':forms.widgets.Select(attrs={'required':True,'class':'col-6'}),
            'return_date': DateInput(attrs={'min':f'{datetime.datetime.now().date()}'}),
            'borrowed_date': DateInput(attrs={'min':f'{datetime.datetime.now().date()}','value':f'{datetime.datetime.now().date()}',
            'required':True})
        }
class InstanceFilterForm(forms.ModelForm):
    book__title=forms.CharField()
    borrower__first_name=forms.CharField()
    borrower__last_name=forms.CharField()
    borrowed_date=forms.CharField()
    class Meta:
        model=Instance
        fields=['id','book__title','borrower__first_name','borrower__last_name','borrowed_date']
        widgets={
            'book__title':forms.widgets.TextInput(attrs={'class':'form-control col-auto'})
        }


