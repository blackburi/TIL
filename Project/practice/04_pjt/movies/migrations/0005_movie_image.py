# Generated by Django 4.2.11 on 2024-04-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, upload_to='%Y/%M/%d'),
        ),
    ]
