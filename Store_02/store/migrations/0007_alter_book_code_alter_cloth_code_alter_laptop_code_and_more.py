# Generated by Django 4.0.2 on 2022-03-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_book_code_cloth_code_laptop_code_mobilephone_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(default='1', max_length=255),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='code',
            field=models.CharField(default='1', max_length=255),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='code',
            field=models.CharField(default='1', max_length=255),
        ),
        migrations.AlterField(
            model_name='mobilephone',
            name='code',
            field=models.CharField(default='1', max_length=255),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='code',
            field=models.CharField(default='1', max_length=255),
        ),
    ]
