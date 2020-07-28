from .models import Product ,ProductImgs
from rest_framework import serializers
# from django.contrib.auth.models import User

class ProductApi(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class ProductImgsApi(serializers.ModelSerializer):
    class Meta:
        model=ProductImgs
        fields='__all__'



        