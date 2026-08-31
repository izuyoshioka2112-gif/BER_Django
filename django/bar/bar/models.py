from django.db import models

# Create your models here.

class  Product(models. Model):
     name = models .CharField(max_length=100)
     price = models.IntegerField(max_length= 500)
     category = models.CharField(max_length=10, default='drink') 

     def __str__(self):
        return self.name

 
