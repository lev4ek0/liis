# Generated by Django 4.0.2 on 2022-02-09 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_articles_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='Article',
        ),
    ]
