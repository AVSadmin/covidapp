# Generated by Django 3.0.4 on 2020-03-19 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdSourceMap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heatmap',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 19, 18, 15, 58, 847819)),
        ),
        migrations.AlterField(
            model_name='markup',
            name='patientEnd',
            field=models.CharField(default=None, max_length=24),
        ),
        migrations.AlterField(
            model_name='markup',
            name='patientStart',
            field=models.CharField(default=None, max_length=24),
        ),
        migrations.AlterField(
            model_name='markup',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 19, 18, 15, 58, 890173)),
        ),
    ]
