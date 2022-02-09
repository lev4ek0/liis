from django.db import models


class Articles(models.Model):
    PUBLIC = 'PUB'
    PRIVATE = 'PRI'
    TypeChoices = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )

    author = models.IntegerField()
    header = models.CharField(max_length=30)
    text = models.CharField(max_length=200)
    creation_date = models.DateTimeField()
    type = models.CharField(max_length=3, choices=TypeChoices, default=PRIVATE)
