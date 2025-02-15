from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=255)
    phone=models.IntegerField(max_length=100)
    email=models.EmailField(max_length=255)
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)

