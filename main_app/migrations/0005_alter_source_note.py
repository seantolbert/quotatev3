# Generated by Django 3.2.7 on 2021-09-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_source_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='note',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
