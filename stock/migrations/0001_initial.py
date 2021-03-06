# Generated by Django 2.2.5 on 2021-06-23 15:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('memo', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('buy', 'Buy'), ('sel', 'Sell')], max_length=3)),
                ('volume', models.FloatField(default=0)),
                ('price', models.FloatField(default=0)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
