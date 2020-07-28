from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from .apis import CartApi , CartItemApi
from rest_framework import viewsets
from .models import Cart , CartItem
# from django.contrib.auth.models import User
# from rest_framework.views import APIView

# from django.views.generic import TemplateView, ListView ,DetailView

# Create your views here.


class cart_list(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartApi
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'orderd']

class cart_item(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemApi
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cart']