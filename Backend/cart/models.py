from django.db import models
from django.db.models import IntegerField, Model
from user.models import Puser
from product.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator

class  Cart (models.Model):
    user = models.ForeignKey(Puser, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now=True)
    orderd = models.BooleanField(default=False)



class  CartItem (models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantatiy = models.PositiveIntegerField(default=1)
    proOrderdPrice = models.DecimalField(max_digits=5,decimal_places=2)

