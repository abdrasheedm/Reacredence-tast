# Generated by Django 5.0.4 on 2024-04-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]
