# Generated by Django 2.2.5 on 2021-06-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advent',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='advent',
            name='part',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='advent',
            name='year',
            field=models.IntegerField(default=2015),
        ),
    ]