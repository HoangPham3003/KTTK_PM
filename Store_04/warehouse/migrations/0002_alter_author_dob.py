# Generated by Django 4.0.2 on 2022-05-16 17:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
