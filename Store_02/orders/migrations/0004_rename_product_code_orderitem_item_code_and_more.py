# Generated by Django 4.0.2 on 2022-03-27 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_order_status_order_order_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product_code',
            new_name='item_code',
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
