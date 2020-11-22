# Generated by Django 3.1.1 on 2020-11-19 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_hotel_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='price',
            field=models.IntegerField(default=5000),
        ),
        migrations.AddField(
            model_name='hotel',
            name='cpn',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
