# Generated by Django 4.0.2 on 2022-05-17 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0005_alter_book_category_alter_book_publisher'),
        ('customer', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_book', to='warehouse.book')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_customer', to='customer.customer')),
            ],
            options={
                'verbose_name_plural': 'Comment',
            },
        ),
    ]