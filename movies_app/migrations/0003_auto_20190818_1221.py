# Generated by Django 2.1.7 on 2019-08-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_movies_movie_subtitles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='id',
        ),
        migrations.AddField(
            model_name='movies',
            name='movie_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]