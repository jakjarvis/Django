# Generated by Django 3.2.5 on 2021-07-29 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advent', '0003_alter_advent_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advent',
            name='part',
        ),
    ]
