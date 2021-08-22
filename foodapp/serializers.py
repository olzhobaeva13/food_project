from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Food
from django.db.models import fields

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username',]

class FoodSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M")

    
    class Meta:
        model = Food
        fields = ['id', 'owner', 'title', 'body', 'created_at', 'price', 'products_list', 'quantity', 'image']
