from django.contrib import admin

from .models import Author,  Book,  Instance, Language, Member

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Instance)

admin.site.register(Language)
admin.site.register(Member)