# Generated by Django 4.0.2 on 2022-03-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.BooleanField(default=False),
        ),
    ]
