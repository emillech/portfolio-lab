# Generated by Django 3.1.5 on 2021-01-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes_giver', '0006_auto_20210113_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]