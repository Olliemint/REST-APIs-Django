# Generated by Django 4.0.5 on 2022-06-08 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_movies_moviedata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedata',
            old_name='durattion',
            new_name='duration',
        ),
    ]
