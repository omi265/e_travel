# Generated by Django 3.1.1 on 2020-12-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20201130_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='no_rooms',
            field=models.IntegerField(null=True),
        ),
    ]
