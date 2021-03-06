# Generated by Django 2.1 on 2018-10-12 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateVal', models.DateField(default=datetime.date.today)),
                ('score', models.IntegerField()),
                ('symptoms', models.TextField()),
                ('relevantFactors', models.TextField()),
            ],
        ),
    ]
