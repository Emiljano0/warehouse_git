# Generated by Django 2.1.7 on 2019-08-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_subtitles',
            field=models.FileField(default='jadajada', upload_to=''),
        ),
    ]
