from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['email', 'password']
