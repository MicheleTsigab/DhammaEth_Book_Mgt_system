from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/',views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',views.AuthorDetailView.as_view(),name='author-detail'),
    path('book/add',views.AddBookView.as_view(),name='add-book'),
    path('author/add',views.AddAuthorView.as_view(),name='add-author'),
    path('member/add',views.AddMemberView.as_view(),name='add-member'),
    path('book/lend',views.LendBookView.as_view(),name='lend-book'),
    path('book/return',views.ReturnBookView.as_view(),name='return-book'),
    path('instance/<int:pk>', views.InstanceDetailView.as_view(), name='instance-detail'),
    path('instances/', views.InstanceFilterView.as_view(), name='instance-list'),
    re_path(
        r'^instance-autocomplete/$'
        ,views.InstanceAutoComplete.as_view(),name='get_instance'
    )
]+ static(settings.STATIC_URL, 
document_root=settings.STATIC_ROOT)