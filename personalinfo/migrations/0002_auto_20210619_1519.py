# Generated by Django 3.1.7 on 2021-06-19 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalinfo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='item',
            new_name='grade',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='price',
            new_name='point',
        ),
    ]