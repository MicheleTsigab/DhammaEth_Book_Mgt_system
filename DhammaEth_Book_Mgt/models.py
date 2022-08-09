from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=300)
    cover=models.ImageField(blank=True, null=True)
    copies=models.IntegerField()

class Admin(models.Model):
    pass
class Member(models.Model):
    dhamma_id=models.CharField(max_length=40,null=True)
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    phone=models.CharField(max_length=40) 
    email=models.EmailField()
    borrowed_books=models.ManyToManyField(Book,through='Borrowed_Book')
class Borrowed_Book(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    borrowed_date=models.DateField(auto_now=True)
    return_date=models.DateField()
    
