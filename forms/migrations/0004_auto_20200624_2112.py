# Generated by Django 3.0.7 on 2020-06-24 20:12

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20200622_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
