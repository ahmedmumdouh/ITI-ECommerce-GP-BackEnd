from .models import Buy
from rest_framework import serializers
# from django.contrib.auth.models import User

class BuyApi(serializers.ModelSerializer):
    class Meta:
        model=Buy
        fields='__all__'





        