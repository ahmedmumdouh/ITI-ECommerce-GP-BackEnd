from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from .apis import CategoryApi 
from rest_framework import viewsets
from .models import Category
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend


# from django.contrib.auth.models import User
# from rest_framework.views import APIView

# from django.views.generic import TemplateView, ListView ,DetailView

# Create your views here.


class category_list(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryApi
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','id']