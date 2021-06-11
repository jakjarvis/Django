# Generated by Django 3.2.3 on 2021-06-10 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_stock_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='stock',
            name='volume',
            field=models.FloatField(default=0),
        ),
    ]
