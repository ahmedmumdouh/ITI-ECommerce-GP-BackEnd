from .models import Puser
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['id', 'first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True} }
        def create(self, validated_data):
            # validated_data = json.loads(validated_data)  
            user = User(
                email=validated_data['email'],
                username=validated_data['username']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user

    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user
    
class PUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model=Puser
        fields= ('id', 'user', 'address', 'phone','avatar')


    def create(self, validated_data):
        # user_data = json.loads(validated_data.pop('user'))  #new
        # print(user_data)
        user_data = validated_data.pop('user')
        user = User(
            first_name= user_data['first_name'],
            last_name= user_data['last_name'],
            username= user_data['username'],
            email= user_data['email'],
            )
        user.set_password(user_data['password'])
        user.save()
        instance = Puser.objects.create(user=user, **validated_data)
        return instance



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=Token
        fields= '__all__'