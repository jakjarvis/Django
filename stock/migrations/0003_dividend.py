# Generated by Django 3.2.5 on 2021-10-16 14:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0002_alter_stock_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dividend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('memo', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('divd', 'Dividend'), ('right', 'Rights Sale')], max_length=5)),
                ('value', models.FloatField(default=0)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
