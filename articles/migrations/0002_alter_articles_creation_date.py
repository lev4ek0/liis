# Generated by Django 4.0.2 on 2022-02-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]