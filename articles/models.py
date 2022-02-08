from django.db import models


class Articles(models.Model):
    class TypeOfArticle(models.TextChoices):
        PUBLIC = 'PUB'
        PRIVATE = 'PRI'

    author = models.IntegerField()
    header = models.CharField(max_length=30)
    text = models.CharField(max_length=200)
    creation_date = models.DateTimeField()
    type = models.CharField(max_length=3, choices=TypeOfArticle, default=TypeOfArticle.PRIVATE)
