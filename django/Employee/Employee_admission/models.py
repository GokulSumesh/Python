from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=30000)

    def __str__(self):
        return self.name
