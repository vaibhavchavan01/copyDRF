# Generated by Django 4.0.2 on 2022-04-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DRFapp', '0002_user_confirm_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
