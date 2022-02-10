from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import User
from .models import Article
from .serializers import ArticleSerializer


def author_decorator(func):

    def decorated(self, request):
        if request.user.is_authenticated:
            if request.user.role == User.AUTHOR:
                response = func(self, request)
            else:
                response = Response({'error': 'Only author can create article.'}, status=status.HTTP_403_FORBIDDEN)
        else:
            response = Response({'error': 'Log in to create article.'}, status=status.HTTP_401_UNAUTHORIZED)
        return response

    return decorated


class ArticleAPIView(APIView):
    serializer_class = ArticleSerializer

    def get(self, request, pk=None):
        if request.user.is_authenticated and request.user.role in [User.AUTHOR, User.SUBSCRIBER]:
            article = Article.objects.all()
        else:
            article = Article.objects.filter(type=Article.PUBLIC)
        if pk:
            article = article.filter(pk=pk)
            response = Response(article.values()[0] if article else {}, status=status.HTTP_200_OK)
        else:
            response = Response(article.values(), status=status.HTTP_200_OK)
        return response

    @author_decorator
    def post(self, request):
        data = request.data
        data['author'] = request.user.pk
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"id": serializer.data.get('id', None)}, status=status.HTTP_201_CREATED)

    @author_decorator
    def put(self, request, pk):
        data = request.data
        try:
            instance = Article.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response({'error': f'Article with id={pk} doesn\'t exist'},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance=instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @author_decorator
    def delete(self, request, pk):
        try:
            Article.objects.get(pk=pk).delete()
        except ObjectDoesNotExist:
            return Response({'error': f'Article with id={pk} doesn\'t exist'},
                            status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
