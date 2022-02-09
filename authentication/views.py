from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError

from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterAPIView(APIView):

    def post(self, request):
        try:
            data = request.data.get('user', {})
            validate_email(data['email'])
            validate_password(data['password'])
            user = User.objects.create_user(email=data['email'], password=data['password'])
            user.save()
            response = Response({'id': user.pk}, status=status.HTTP_200_OK)
        except KeyError:
            response = Response({'error': 'Wrong data format.'}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            response = Response({'error': 'User with this email address already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            response = Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)
        return response


class LoginAPIView(APIView):

    def post(self, request):
        try:
            data = request.data.get('user', {})
            user = authenticate(email=data['email'], password=data['password'])
            if user is not None:
                login(request, user)
                response = Response(status=status.HTTP_200_OK)
            else:
                response = Response({'error': 'Wrong email or password.'}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError:
            response = Response({'error': 'Wrong data format.'}, status=status.HTTP_400_BAD_REQUEST)
        return response


class LogoutAPIView(APIView):

    def post(self, request):
        logout(request)
        response = Response(status=status.HTTP_200_OK)
        return response
