from datetime import date
import email
from unicodedata import name
from django.db import models
from sqlalchemy import desc

# Create your models here.
class Contract(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
    
    

