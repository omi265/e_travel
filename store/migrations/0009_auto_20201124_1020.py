# Generated by Django 3.1.1 on 2020-11-24 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20201124_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='no_stops',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='flights',
            name='stop_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
