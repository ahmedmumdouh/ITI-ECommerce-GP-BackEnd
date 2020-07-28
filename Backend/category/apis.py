from .models import Category
from rest_framework import serializers
# from django.contrib.auth.models import User

class CategoryApi(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'



        