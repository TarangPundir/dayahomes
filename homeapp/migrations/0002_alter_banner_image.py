# Generated by Django 3.2.19 on 2023-07-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='banner/'),
        ),
    ]
