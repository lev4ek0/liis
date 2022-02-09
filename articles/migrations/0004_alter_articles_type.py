# Generated by Django 4.0.2 on 2022-02-09 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='type',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private')], default='Private', max_length=10),
        ),
    ]