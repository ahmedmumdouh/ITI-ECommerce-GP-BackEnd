from django.db import models
from user.models import Puser
from cart.models import Cart

class  Buy (models.Model):
    cart = models.ForeignKey(Cart,null=True ,on_delete=models.CASCADE)
    user = models.ForeignKey(Puser, on_delete=models.CASCADE)
    ship_To = models.TextField(default='')
    totalPrice = models.DecimalField(max_digits=9, decimal_places=2 ,default=0)
    orderdDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.full_name + " - " +str(self.cart.id)
