# Generated by Django 4.0.2 on 2022-05-16 17:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('dob', models.DateTimeField(default=datetime.datetime.now)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Author',
                'ordering': ('-fullname',),
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publisher_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Publisher',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Category',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('number_of_page', models.DecimalField(decimal_places=0, max_digits=8)),
                ('date_publish', models.DateTimeField(default=datetime.datetime.now)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=8)),
                ('price', models.DecimalField(decimal_places=0, max_digits=8)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='warehouse.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='warehouse.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_creator', to=settings.AUTH_USER_MODEL)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='warehouse.publisher')),
            ],
            options={
                'verbose_name_plural': 'Books',
                'ordering': ('-created',),
            },
        ),
    ]
