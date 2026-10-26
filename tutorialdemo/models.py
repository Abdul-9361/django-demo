from django.db import models

# Create your models here.

class product(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Document(models.Model):
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to="documents/")

    def __str__(self):
        return self.name

from django.db import models


class Expense(models.Model):
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item
        