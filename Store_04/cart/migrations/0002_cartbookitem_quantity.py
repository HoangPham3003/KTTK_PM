# Generated by Django 4.0.2 on 2022-05-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartbookitem',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=8),
        ),
    ]