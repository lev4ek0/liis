# Generated by Django 4.0.2 on 2022-02-10 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_articles_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], max_length=10),
        ),
    ]
