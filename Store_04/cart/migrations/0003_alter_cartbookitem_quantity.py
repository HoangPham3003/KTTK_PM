# Generated by Django 4.0.2 on 2022-05-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cartbookitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartbookitem',
            name='quantity',
            field=models.DecimalField(decimal_places=0, max_digits=8),
        ),
    ]
