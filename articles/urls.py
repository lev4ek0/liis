from django.urls import path

from .views import ArticlesAPIView

urlpatterns = [
    path('articles/', ArticlesAPIView.as_view()),
    path('articles/<int:pk>/', ArticlesAPIView.as_view())
]