# Generated by Django 3.2.7 on 2021-09-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210910_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='sources',
            field=models.ManyToManyField(to='main_app.Source'),
        ),
    ]
