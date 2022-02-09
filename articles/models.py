from django.db import models


class ArticlesManager(models.Manager):

    def create_article(self, author, header, text, type):
        article = self.model(author=author, header=header, text=text, type=type)
        article.save()
        return article


class Articles(models.Model):
    PUBLIC = 'Public'
    PRIVATE = 'Private'
    TypeChoices = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )

    author = models.IntegerField()
    header = models.CharField(max_length=30)
    text = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=10, choices=TypeChoices, default=PRIVATE)

    objects = ArticlesManager()
