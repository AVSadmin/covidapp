# Generated by Django 3.0.4 on 2020-03-19 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeatMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.IntegerField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 3, 19, 17, 19, 7, 63366))),
            ],
        ),
        migrations.CreateModel(
            name='MarkUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorder', models.CharField(max_length=64)),
                ('ip', models.CharField(max_length=128)),
                ('patientId', models.CharField(max_length=12)),
                ('patientStart', models.DateTimeField(default=None)),
                ('patientEnd', models.DateTimeField(default=None)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 3, 19, 17, 19, 7, 102723))),
                ('active', models.IntegerField(default=0)),
            ],
        ),
    ]
