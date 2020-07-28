from django.shortcuts import render

from rest_framework.response import Response
from .apis import BuyApi
from rest_framework import viewsets
from .models import Buy
# from django.contrib.auth.models import User
# from rest_framework.views import APIView

# from django.views.generic import TemplateView, ListView ,DetailView

# Create your views here.


class buy_item(viewsets.ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuyApi