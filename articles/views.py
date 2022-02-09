from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import User
from .models import Article
from .serializers import ArticleSerializer


class ArticleAPIView(APIView):
    serializer_class = ArticleSerializer

    def get(self, request, pk=None):
        if request.user.is_authenticated and (request.user.role == User.AUTHOR or request.user.role == User.SUBSCRIBER):
            a = Article.objects.all()
        else:
            a = Article.objects.filter(type=Article.PUBLIC)
        if pk is not None:
            a = a.filter(pk=pk)
        response = Response(a.values(), status=status.HTTP_200_OK)
        return response

    def post(self, request):
        if request.user.is_authenticated:
            if request.user.role == User.AUTHOR:
                data = request.data.get("article", {})
                data['author'] = request.user.pk
                serializer = self.serializer_class(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                response = Response({"id": serializer.data.get('id', None)}, status=status.HTTP_200_OK)
            else:
                response = Response({'error': 'Only author can create article.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = Response({'error': 'Log in to create article.'}, status=status.HTTP_400_BAD_REQUEST)
        return response

    def put(self, request, pk):
        if request.user.is_authenticated:
            if request.user.role == User.AUTHOR:
                data = request.data.get("article", {})
                instance = Article.objects.get(pk=pk)
                serializer = self.serializer_class(instance=instance, data=data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                response = Response({"id": pk}, status=status.HTTP_200_OK)
            else:
                response = Response({'error': 'Only author can create article.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = Response({'error': 'Log in to create article.'}, status=status.HTTP_400_BAD_REQUEST)
        return response

    def delete(self, request, pk):
        if request.user.is_authenticated:
            if request.user.role == User.AUTHOR:
                try:
                    instance = Article.objects.get(pk=pk)
                except ObjectDoesNotExist:
                    return Response({'error': f'Article with id={pk} doesn\'t exist'},
                                    status=status.HTTP_400_BAD_REQUEST)
                instance.delete()
                response = Response({"id": pk}, status=status.HTTP_200_OK)
            else:
                response = Response({'error': 'Only author can create article.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = Response({'error': 'Log in to create article.'}, status=status.HTTP_400_BAD_REQUEST)
        return response
