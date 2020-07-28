from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .apis import ProductApi , ProductImgsApi
from rest_framework import viewsets
from .models import Product , ProductImgs
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class product_list(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductApi
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','id','in_stock','category','supplier','price']

class product_list_imgs(viewsets.ModelViewSet):
    queryset = ProductImgs.objects.all()
    serializer_class = ProductImgsApi
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','product']