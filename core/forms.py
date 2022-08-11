from .models import Book
from django import forms
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