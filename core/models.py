from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Language(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class Meta:
        ordering = ['last_name','-first_name']
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    def __str__(self):
        return self.first_name + ' '+self.last_name
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL, null=True)
    cover=models.ImageField(upload_to='images',blank=True, null=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True,blank=True)
    class Meta:
        ordering = ['title']
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class Admin(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
class Member(models.Model):
    dhamma_id=models.CharField(max_length=40,null=True,blank=True)
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    phone=models.CharField(max_length=40,null=True,blank=True) 
    email=models.EmailField(null=True,blank=True)
    class Meta:
        ordering = ['last_name','-first_name']
    def __str__(self):
        return self.first_name + ' '+self.last_name
class Instance(models.Model):
    """A specific copy of a Book that is actually borrow-able
    """
    id = models.BigAutoField(primary_key=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    status=models.ForeignKey('BorrowedBook',on_delete=models.SET_NULL,null=True,blank=True)
    class Meta:
        ordering = ['book']
class BorrowedBook(models.Model):
    #Book=models.ForeignKey(Instance,on_delete=models.CASCADE)
    borrower = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrowed_date=models.DateField(auto_now=True,null=True)
    return_date=models.DateField(null=True)
    class Meta:
        ordering = ['borrowed_date']
    
