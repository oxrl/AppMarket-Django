# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-07 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Marca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('marks', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Marca.Mark')),
            ],
        ),
    ]
