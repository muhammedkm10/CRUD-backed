from rest_framework import serializers
from .models import User


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','phone', 'password','image']  # Add or remove fields as needed


   