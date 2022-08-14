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
            'borrower__dhamma_id':['exact'],
            'borrower__first_name':['contains'],
            'borrowed_date':['lt','gt']
            
        }
class InstanceSFilter(django_filters.FilterSet):
    
    class Meta:
        model = Instance
        fields = {
        'id':['exact'],
        'book__title':['contains']
        
        }