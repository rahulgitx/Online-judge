from django.db import models

# Create your models here.
class Contacts(models.Model):
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    name=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
