# Generated by Django 4.0.2 on 2022-03-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DRFapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]