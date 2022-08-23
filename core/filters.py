import django_filters

from .models import  Instance
def borrow_instance(request):
    pass
class InstanceFilter(django_filters.FilterSet):
    class Meta:
        model=Instance
        fields={
            'id':['exact'],
            'book__title':['contains'],
            'borrower__last_name':['contains'],
            'borrower__first_name':['contains'],
            'borrowed_date':['exact']
            
        }
class AvailableBooksFilter(django_filters.FilterSet): 
    class Meta:
        model = Instance
        fields = {
        'book__title':['contains']
        }