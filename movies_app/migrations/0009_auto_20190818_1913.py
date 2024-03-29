# Generated by Django 2.1.7 on 2019-08-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0008_auto_20190818_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='movie_format',
            new_name='movie_quality',
        ),
        migrations.AlterField(
            model_name='movies',
            name='movie_release_date',
            field=models.DateField(default='0000', verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='movies',
            name='movie_subtitles',
            field=models.FileField(default='Planet Earth Subtitles', upload_to=''),
        ),
        migrations.AlterField(
            model_name='movies',
            name='movie_thumbnail',
            field=models.FileField(default='Planet Earth thumbnail', upload_to=''),
        ),
    ]
