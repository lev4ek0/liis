from django.urls import path

from .views import ArticleAPIView

urlpatterns = [
    path('articles/', ArticleAPIView.as_view()),
    path('articles/<int:pk>/', ArticleAPIView.as_view())
]