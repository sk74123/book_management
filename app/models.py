from django.db import models
from datetime import date, datetime, timedelta

# Create your models here.

class Author(models.Model):
    Name= models.CharField(max_length=40)
    Email= models.EmailField()

    def __str__(self):
        return self.Name
    
    class Meta:
        ordering= ["Name"]


class Book(models.Model):
    Name = models.CharField(max_length=100)
    Author=models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Reader(models.Model):
    Name= models.CharField(max_length=100)
    Email=models.EmailField()
    Phone= models.IntegerField()

    def __str__(self):
        return self.Name

def expiry():
    return date.today() + timedelta(days=10)

class Borrow_book(models.Model):
    Reader=models.OneToOneField(Reader, on_delete=models.CASCADE)
    Book= models.ManyToManyField(Book)
    Issued_on= models.DateField(auto_now_add=True)
    Submit_by= models.DateField(default=expiry)
    Returned= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.Reader}"