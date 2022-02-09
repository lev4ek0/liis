# Generated by Django 4.0.2 on 2022-02-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.IntegerField()),
                ('header', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField()),
                ('type', models.CharField(choices=[('PUB', 'Public'), ('PRI', 'Private')], default='PRI', max_length=3)),
            ],
        ),
    ]