# Generated by Django 4.0.2 on 2022-02-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_articles_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
