from django.db import models

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=20 ,null=False ,unique=True)
    desc = models.TextField(max_length=500 ,default='No Added Description for this Category')

    def __str__(self):
        return self.name
