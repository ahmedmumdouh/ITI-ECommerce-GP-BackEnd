from .models import Cart , CartItem
from rest_framework import serializers
# from django.contrib.auth.models import User

class CartApi(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'


class CartItemApi(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields='__all__'


        