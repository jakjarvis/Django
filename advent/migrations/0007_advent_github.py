# Generated by Django 3.2.5 on 2021-07-29 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advent', '0006_remove_advent_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='advent',
            name='github',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]