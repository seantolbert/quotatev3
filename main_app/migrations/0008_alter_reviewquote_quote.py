# Generated by Django 3.2.7 on 2021-09-20 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_quote_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewquote',
            name='quote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.quote'),
        ),
    ]