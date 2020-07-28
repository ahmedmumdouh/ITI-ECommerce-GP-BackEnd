from django.db import models
from django.db.models import IntegerField, Model
from datetime import datetime    
from user.models import Puser
from category.models import Category

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=20 , null=False)
    desc = models.TextField(max_length=1000 , default= 'No Added Description For this Product')
    quantity = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(9999),
            MinValueValidator(0)
        ]
     )
    photo = models.ImageField(
        max_length=255,
        upload_to ='product_photos/',default='product_photos/No_image_available.svg.png')
    # quantity =  fields.IntegerRangeField(min_value=0, max_value=999)
    price =  models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(999999)],
        null=False)
    created_date = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=False)
    supplier = models.ForeignKey(Puser, on_delete=models.CASCADE , blank = False ,null = False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , blank = False ,null = False)

    def __str__(self):
        return self.name

class ProductImgs (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , blank = False ,null = False)
    photos = models.ImageField(
        max_length=255,
        upload_to ='product_imgs/',default='product_photos/No_image_available.svg.png')
