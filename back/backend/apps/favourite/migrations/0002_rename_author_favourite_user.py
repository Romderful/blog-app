# Generated by Django 4.0.4 on 2022-04-23 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favourite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favourite',
            old_name='author',
            new_name='user',
        ),
    ]
