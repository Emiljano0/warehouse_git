# Generated by Django 2.1.7 on 2019-08-18 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentaries_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documentaries',
            old_name='documentary_box_office',
            new_name='documentary_gross',
        ),
    ]
