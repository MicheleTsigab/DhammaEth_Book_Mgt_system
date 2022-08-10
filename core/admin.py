from django.contrib import admin

from .models import Author,  Book, BorrowedBook,  Instance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Instance)
admin.site.register(BorrowedBook)
