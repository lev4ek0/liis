from django.urls import path

from .views import ArticleAPIView

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:pk>/', ArticleAPIView.as_view())
]
