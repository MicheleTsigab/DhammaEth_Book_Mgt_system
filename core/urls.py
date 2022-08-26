from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<int:fk>/instance/add',views.AddInstanceView.as_view(),name='add-instance'),
    path('authors/',views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',views.AuthorDetailView.as_view(),name='author-detail'),
    path('book/add',views.AddBookView.as_view(),name='add-book'),
    path('author/add',views.AddAuthorView.as_view(),name='add-author'),
    path('member/add',views.AddMemberView.as_view(),name='add-member'),
    path('language/add',views.AddLanguageView.as_view(),name='add-lang'),
    path('book/lend',views.AvailableBookView.as_view(),name='lend-book'),
    path('book/return',views.BorrowedBookView.as_view(),name='return-book'),
    path('instance/<int:pk>/lend',views.LendInstance.as_view(),name='lend-instance'),
    path('instance/<int:pk>/return',views.ReturnInstance,name='return-instance'),
    path('instance/<int:pk>', views.InstanceDetailView.as_view(), name='instance-detail'),
    path('instances/', views.InstanceFilterView.as_view(), name='instance-list'),
    path('books/search/',views.BookFilterView.as_view(),name='search-book')
    
]+ static(settings.STATIC_URL, 
document_root=settings.STATIC_ROOT)