# Generated by Django 3.2.7 on 2021-09-21 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_quote_background'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='background',
        ),
    ]
