from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')

    def validate(self, attrs):
        password = attrs['password']
        email = attrs['email']
        validate_email(email)
        validate_password(password)
        return {'password': password, 'email': email}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
