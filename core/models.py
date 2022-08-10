from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=200)
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL, null=True)
    cover=models.ImageField(blank=True, null=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True,blank=True)
class Admin(models.Model):
    pass
class Member(models.Model):
    dhamma_id=models.CharField(max_length=40,null=True,blank=True)
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    phone=models.CharField(max_length=40,null=True,blank=True) 
    email=models.EmailField(null=True,blank=True)
class Instance(models.Model):
    """A specific copy of a Book that is actually borrow-able
    """
    id = models.BigAutoField(primary_key=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    status=models.ForeignKey('BorrowedBook',on_delete=models.SET_NULL,null=True,blank=True)
class BorrowedBook(models.Model):
    #Book=models.ForeignKey(Instance,on_delete=models.CASCADE)
    borrower = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrowed_date=models.DateField(auto_now=True,null=True)
    return_date=models.DateField(null=True)
    
