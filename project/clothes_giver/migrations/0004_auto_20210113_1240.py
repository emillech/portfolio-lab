# Generated by Django 3.1.5 on 2021-01-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes_giver', '0003_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.IntegerField(choices=[(1, 'Foundation'), (2, 'Non-governmental organization'), (3, 'Local collection')], default=1),
        ),
    ]